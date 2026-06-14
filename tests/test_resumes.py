from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_resumes():
    response = client.get("/resumes")

    assert response.status_code == 200