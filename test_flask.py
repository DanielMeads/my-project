import os
import tempfile
import pytest

from main import app


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_get_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_post_new_user_returns_302(client):
    response = client.post("/newuser", data={"username": "Jon"})
    assert response.status_code == 302
