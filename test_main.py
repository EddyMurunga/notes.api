from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_signup():
    response = client.post("/auth/signup", json={
        "username": "testuser",
        "password": "testpass123"
    })
    # 200 if first time, 400 if user already exists
    assert response.status_code in [200, 400]

def test_login():
    # First ensure user exists
    client.post("/auth/signup", json={
        "username": "testuser2",
        "password": "testpass123"
    })
    response = client.post("/auth/login", data={
        "username": "testuser2",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_note_authenticated():
    # Sign up and login to get token
    client.post("/auth/signup", json={
        "username": "noteuser",
        "password": "testpass123"
    })
    login = client.post("/auth/login", data={
        "username": "noteuser",
        "password": "testpass123"
    })
    token = login.json()["access_token"]
    
    # Create note with token
    response = client.post("/notes",
        json={"text": "My test note"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["text"] == "My test note"

def test_create_note_unauthenticated():
    response = client.post("/notes", json={"text": "Should fail"})
    assert response.status_code == 401