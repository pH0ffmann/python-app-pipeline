# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the simple Flask app!"}

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "UP"}

def test_echo(client):
    response = client.post('/echo', json={"test": "data"})
    assert response.status_code == 200
    assert response.get_json() == {"received": {"test": "data"}}

def test_add_item(client):
    response = client.post('/items', json={"item": "new_item"})
    assert response.status_code == 201
    assert "Item 'new_item' added successfully!" in response.get_json().get("message")

def test_get_items(client):
    response = client.get('/items')
    assert response.status_code == 200
    assert "items" in response.get_json()