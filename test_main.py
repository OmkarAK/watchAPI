from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"API health check successful"}

def test_read_builts():
    response = client.get("/v0/built/?limit=12702")
    assert response.status_code == 200
    assert len(response.json()) == 12702

# def test_read_built():
#     response = client.get('/v0/build/14')
#     assert response.status_code == 200
#     assert response.json().get("serial") == 14

def test_read_num():
    response = client.get("/v0/num/?limit=12702")
    assert response.status_code == 200
    assert len(response.json()) == 12702