from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_signup():
    response = client.post("/auth/signup", json={
        "username": "testuser",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_login():
    response = client.post("/auth/login", data={
        "username": "testuser",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()