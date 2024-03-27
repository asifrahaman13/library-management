
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_signup_success():
    payload = {"username": "test_user", "password": "test_password"}
    response = client.post("/signup", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}


def test_signup_failure():
    payload = {"username": "test_user", "password": "test_password"}
    response = client.post("/auth/signup", json=payload)
    assert response.status_code == 400
    assert response.json() == {"message": "User creation failed"}


def test_login_success():
    payload = {"username": "test_user", "password": "test_password"}
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_failure_username_missing():
    payload = {"password": "test_password"}
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 422


def test_login_failure_password_missing():
    payload = {"username": "test_user"}
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 422


def test_login_failure_user_not_found():
    payload = {"username": "non_existing_user", "password": "test_password"}
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 404


def test_login_failure_invalid_password():
    payload = {"username": "test_user", "password": "invalid_password"}
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 401
