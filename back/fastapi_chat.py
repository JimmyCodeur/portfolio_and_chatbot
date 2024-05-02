from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bs4 import BeautifulSoup
import re
from typing import List
from openai import AzureOpenAI
import os
import sys
from config import AZURE_OPENAI_KEY

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



client = AzureOpenAI(
    azure_endpoint="https://openai-lok.openai.azure.com/",
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-15-preview"
)

class Message(BaseModel):
    sender: str
    message: str
    
class ChatRequest(BaseModel):
    system: str = f"you are an assistant who helps answer questions in my portfolio "
    history: List[Message]
    temperature: float = 0.7
    max_tokens: int = 800
    top_p: float = 0.95
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0

def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = ' '.join(soup.stripped_strings)
    text = re.sub(r'<[^>]+>', '', text) 
    return text

@app.post("/generate-text")
async def generate_text(request: ChatRequest):
    try:
        front_dir = os.path.abspath(os.path.join('front'))
        with open(os.path.join(front_dir, 'index.html'), 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        text_from_html = str(extract_text_from_html(html_content))
        history_with_html = [Message(sender="user", message=text_from_html)] 
        history_with_html.extend(request.history)

        message_text = [
            {"role": "user", "content": msg.message} for msg in history_with_html
        ]

        completion = client.chat.completions.create(
            model="gpt35-latest",
            messages=message_text,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            top_p=request.top_p,
            frequency_penalty=request.frequency_penalty,
            presence_penalty=request.presence_penalty
        )
        completion_dict = completion.model_dump()
        choices = completion_dict.get('choices', [])
        if choices:
            first_choice = choices[0]
            generated_text = first_choice.get('message', {}).get(
                'content', 'No content available')
            response_data = {
                "response": generated_text,
                "config": {
                    "temperature": request.temperature,
                    "max_tokens": request.max_tokens,
                    "top_p": request.top_p,
                    "frequency_penalty": request.frequency_penalty,
                    "presence_penalty": request.presence_penalty
                }
            }
            return JSONResponse(content=response_data)
        else:
            return JSONResponse(content={"error": "No choices available"}, status_code=500)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8008)
