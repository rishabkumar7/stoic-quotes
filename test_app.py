import pytest
from flask import json
from app import app, quotes

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_data(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<html>' in response.data
    assert b'</html>' in response.data

def test_get_quote_status_code(client):
    response = client.get('/api/random')
    assert response.status_code == 200

def test_get_quote_data(client):
    response = client.get('/api/random')
    data = json.loads(response.get_data())
    assert 'quote' in data
    assert 'author' in data

def test_search_status_code(client):
    response = client.get('/api/search/wealth')
    assert response.status_code == 200

def test_search_data(client):
    response = client.get('/api/search/wealth')
    data = json.loads(response.get_data())
    assert 'results' in data