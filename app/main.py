from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session


import app.models as models
import app.schemas as schemas

from app.database import Base, engine, SessionLocal
from app.repository import Repository

# creates database
Base.metadata.create_all(engine)
repository = Repository()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


app = FastAPI()
api_router = APIRouter()


@api_router.get("/")
def get_all_books(session: Session = Depends(get_session)):
    books = repository.get_all(models.Book, session)
    return books


@api_router.post("/")
def add_book(book: schemas.Book, session: Session = Depends(get_session)):
    book = models.Book(title=book.title, author=book.author, price=book.price)
    repository.add_object(session, book)
    return book


@api_router.get("/{book_id}")
def get_book(book_id: int, session: Session = Depends(get_session)):
    return repository.get_one(book_id, session, models.Book)


@api_router.put("/{book_id}")
def update_book(
    book_id: int, book: schemas.Book, session: Session = Depends(get_session)
):
    book_updated = repository.get_one(book_id, session)
    book_updated.title = book.title
    book_updated.author = book.author
    book_updated.price = book.price
    session.commit()
    return book_updated


@api_router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    return repository.delete_object(book_id, models.Book, session)


app.include_router(api_router)
