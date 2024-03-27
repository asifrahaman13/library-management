import pytest
from fastapi.testclient import TestClient
from src.main import app
from tests.helper.helper import random_string


random_password = "ODCOmU1k"
client = TestClient(app)


@pytest.fixture(scope="module")
def auth_token():
    # Perform signup to create a test user
    signup_payload = {"username": "test_user", "password": random_password}
    client.post("/auth/signup", json=signup_payload)

    # Perform login to obtain an authentication token
    login_payload = {"username": "test_user", "password": random_password}
    response = client.post("/auth/login", json=login_payload)
    return response.json().get("access_token")


def test_create_book(auth_token):
    book_data = {
        "Title": "Book from the sample user",
        "Authors": "Author Name from sample user",
        "Publication_Date": "2022-01-01",
        "ISBN": random_string,
        "Description": "Oh its updated.My book updated. Sample book description. This is nice description",
    }
    response = client.post(
        "/api/books", json=book_data, headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200


def test_get_all_books(auth_token):
    response = client.get(
        "/api/books", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200


def test_get_all_books(auth_token):
    response = client.get(
        "/api/books", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200


def test_get_book_by_id(auth_token):
    isbn = random_string
    response = client.get(
        f"/api/books/{isbn}", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200


def test_update_book(auth_token):
    isbn = random_string
    update_data = {
        "Title": "Book from the sample user",
        "Authors": "Author Name from sample user",
        "Publication_Date": "2022-01-01",
        "ISBN": random_string,
        "Description": "Oh its updated.My book updated. Sample book description. This is nice description",
    }
    response = client.put(
        f"/api/books/{isbn}",
        json=update_data,
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    # Add more assertions as needed


def test_delete_book(auth_token):
    isbn = random_string
    response = client.delete(
        f"/api/books/{isbn}", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200

