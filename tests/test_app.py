import pytest
from src.app import create_app, num_tokens_from_string

@pytest.fixture
def client():
  app = create_app()
  app.config['TESTING'] = True

  with app.test_client() as client:
    yield client

def test_num_tokens_from_string():
  assert num_tokens_from_string("tiktoken is great!", "cl100k_base") == 5
  assert num_tokens_from_string("another test", "cl100k_base") == 2

def test_get_num_tokens_endpoint(client):
  response = client.post('/tokens', json={"text": "tiktoken is great!"})
  json_data = response.get_json()
  assert response.status_code == 200
  assert json_data["tokens"] == 5

  response = client.post('/tokens', json={"text": "another test", "encoding": "cl100k_base"})
  json_data = response.get_json()
  assert response.status_code == 200
  assert json_data["tokens"] == 2
