import pytest
from app import app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
def test_404_error_handling(client):
    response = client.get('/nonexistent-route')
    assert response.status_code == 404
    assert b'Your custom 404 message' in response.data
