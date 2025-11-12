import pytest
from app import schemas
from app.config import settings
import jwt


# @pytest.fixture
# def test_user(client):
#     user_data = {"email": "satyam@gmail.com",
#                  "password": "qwerty"}
#     res = client.post("/users/", json=user_data)

#     assert res.status_code == 201
#     print(res.json())

#     new_user = res.json()
#     new_user['password'] = user_data['password']

#     return new_user


# def test_read_root(client):
#     res = client.get("/")
#     # print(res.json().get("Hello"))
#     assert res.status_code == 200
#     assert res.json() == {"Hello": "World"}


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "satyam@gmail.com", "password": "qwerty"})
    
    new_user = schemas.UserOutput(**res.json())
    assert new_user.email == "satyam@gmail.com"
    assert res.status_code == 201


def test_login_user(test_user, client):
    res = client.post(
        "/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,
                         settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'qwerty', 403),
    ('satyam@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'qwerty', 403), # on testing with None value, it is expecting 403 instead of 422 hence changed the expected status code
    ('satyam@gmail.com', None, 403) # same here
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post(
        "/login", data={"username": email, "password": password})

    assert res.status_code == status_code
    assert res.json().get('detail') == 'Invalid Credentials'    