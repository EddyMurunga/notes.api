from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Notes API is running"}

def test_create_note():
    response = client.post("/notes", json={"text": "Test note"})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Test note"
    assert "id" in data

def test_get_notes():
    response = client.get("/notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)