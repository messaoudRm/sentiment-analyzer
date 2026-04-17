from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def testRoot():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Sentiment Analyzer Microservice is running"




