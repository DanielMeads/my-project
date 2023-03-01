import os
import tempfile
import pytest

from main import app


@pytest.fixture
def client():
    db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True

    with app.app.test_client() as client:
        with app.app.app_context():
            app.init_db()
        yield client

    os.close(db_fd)
    os.unlink(our_app.app.config['DATABASE'])

def test_get_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_post_new_user_returns_201(client):
    response = client.post("/newuser", data={"name": "Jon"})
    assert response.status_code == 201