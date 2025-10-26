from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def testRoot():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Sentiment Analyzer Microservice is running"

def testPositiveSentimentAnalyze():
    payload = {"text": "I love The Dark Knight, it's an amazing movie!"}
    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "label" in data
    assert "score" in data
    assert data["score"] > 0
    print("Positive test:", data)

def testNegativeSentimentAnalyze():
    payload = {"text": "The last season of Game of Thrones was terrible!"}
    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "label" in data
    assert "score" in data
    print("Negative test:", data)


