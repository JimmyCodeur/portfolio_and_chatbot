from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ..back.fastapi_chat import ChatRequest, app

client = TestClient(app)

def test_generate_text():
    request = ChatRequest(
        system="Test system",
        history=[{"sender": "user", "message": "Test message 1"}],
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    response = client.post("/generate-text", json=request.dict())
    assert response.status_code == 200
    assert "response" in response.json()


