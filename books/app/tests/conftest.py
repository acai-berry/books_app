import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client


@pytest.fixture()
def test_request_payload():
    return {
        "title": "something",
        "author": "something else",
        "price": 10.0,
    }


@pytest.fixture()
def test_response_payload():
    return {
        "id": 1,
        "title": "something",
        "author": "something else",
        "price": 10.0,
    }


@pytest.fixture()
def test_update_request_data():
    return {
        "title": "test_title1_updated",
        "author": "test_author1",
        "price": 9.99,
    }


@pytest.fixture()
def test_update_response_data():
    return {
        "id": 1,
        "title": "test_title1_updated",
        "author": "test_author1",
        "price": 9.99,
    }
