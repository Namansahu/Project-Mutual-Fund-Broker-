from fastapi.testclient import TestClient
from app.__init__ import app

client = TestClient(app)

def test_register():
    response = client.post("/register", json={"email": "test@example.com", "password": "test123"})
    assert response.status_code == 200

def test_login():
    response = client.post("/login", json={"email": "test@example.com", "password": "test123"})
    assert response.status_code == 200

