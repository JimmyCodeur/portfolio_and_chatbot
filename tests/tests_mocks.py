from fastapi.testclient import TestClient
from back.fastapi_chat import app
from unittest.mock import MagicMock

client = TestClient(app)

mock_openai = MagicMock()

mock_openai.chat.completions.create.return_value = {
    "choices": [
        {
            "message": {
                "content": "who is jimmy fernandez?"
            }
        }
    ]
}

app.dependency_overrides[client] = mock_openai

def test_generate_text_with_mock():
    response = client.post("/generate-text", json={
        "system": "you are an assistant who helps answer questions in my portfolio",
        "history": [{"sender": "user", "message": ""}],
        "temperature": 0.7,
        "max_tokens": 800,
        "top_p": 0.95,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    })

    assert response.status_code == 200
    print(response.status_code)
    assert response.json()["response"] == "jimmy fernandez"
