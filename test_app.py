import pytest
from flask import json
from app import app, container


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

from unittest.mock import patch 

@patch.object(container, 'read_all_items', return_value=[
    {'id': 'test_doc_1', 'quotes': [{'quote': 'Test Quote 1', 'author': 'Test Author'}]},
    {'id': 'test_doc_2', 'quotes': [{'quote': 'Another Test Quote', 'author': 'Another Author'}]}
])

def test_home_status_code(read_all_items, client):
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