import pytest
from fastapi.testclient import TestClient

from app.repository import get_session
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from config import get_settings


engine = create_engine(
    get_settings().TEST_DATABASE, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture
def client():
    app.dependency_overrides[get_session] = override_get_db
    with TestClient(app) as client:
        yield client
