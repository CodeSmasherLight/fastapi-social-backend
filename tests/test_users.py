from fastapi.testclient import TestClient
from app.main import app
from app import schemas


client = TestClient(app)

def test_read_root():
    res = client.get("/")
    # print(res.json().get("Hello"))
    assert res.status_code == 200
    assert res.json() == {"Hello": "World"}


def test_create_user():
    res = client.post(
        "/users/", json={"email": "satyam@gmail.com", "password": "qwerty"})
    
    new_user = schemas.UserOutput(**res.json())
    assert new_user.email == "satyam@gmail.com"
    assert res.status_code == 201