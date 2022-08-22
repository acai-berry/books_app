from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.main import app, get_session

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_session] = override_get_db

client = TestClient(app)


def test_create_book():
    response = client.post(
        "/",
        json={"title": "test_title1", "author": "test_author1", "price": 9.99},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test_title1"
    assert data["author"] == "test_author1"
    assert data["price"] == 9.99
    assert "id" in data
    book_id = data["id"]

    response = client.get(f"/{book_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test_title1"
    assert data["author"] == "test_author1"
    assert data["price"] == 9.99
    assert data["id"] == book_id


def test_get_all_books():
    response = client.get("/")
    events = response.json()
    assert response.status_code == 200
    assert len(events) == 1

def test_get_a_book_happy_path():
    response = client.get(f"/{1}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test_title1"
    assert data["author"] == "test_author1"
    assert data["price"] == 9.99
    assert data["id"] == 1

def test_get_a_book_no_book():
    response = client.get(f"/{2}")
    assert response.status_code == 404

def test_update_a_book():
    response = client.put(f"/{1}",
        json={"title": "test_title1_updated", "author": "test_author1", "price": 9.99},
    )
    assert response.status_code == 200

    response = client.get(f"/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test_title1_updated"
    assert data["author"] == "test_author1"
    assert data["price"] == 9.99
    assert data["id"] == 1

def test_delete_a_book():
    response = client.delete(f"/{1}")
    assert response.status_code == 200

    response = client.get(f"/{1}")
    assert response.status_code == 404

def test_delete_no_book():
    response = client.delete(f"/{2}")
    assert response.status_code == 404
