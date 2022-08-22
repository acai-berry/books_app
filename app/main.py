from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


import app.models as models
import app.schemas as schemas

from app.database import Base, engine,  SessionLocal

#creates database
Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()
api_router = APIRouter()


@api_router.get("/")
def get_all_books(session:Session = Depends(get_session)):
    books = session.query(models.Book).all()
    return books

@api_router.post("/")
def add_book(book:schemas.Book, session: Session = Depends(get_session)):
    book = models.Book(title = book.title, author = book.author, price = book.price)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


@api_router.get("/{book_id}")
def get_book(book_id:int, session: Session = Depends(get_session)):
    book = session.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(
            status_code=404, detail=f"Book with ID {book_id} not found"
        )
    return book


@api_router.put("/{book_id}")
def update_book(book_id:int, book:schemas.Book, session:Session = Depends(get_session)):
    book_updated = session.query(models.Book).get(book_id)
    if not book_updated:
        raise HTTPException(
            status_code=404, detail=f"Book with ID {book_id} not found"
        )
    book_updated.title = book.title
    book_updated.author = book.author
    book_updated.price = book.price
    session.commit()
    return book_updated


@api_router.delete("/{book_id}")
def delete_book(book_id:int, session:Session = Depends(get_session)):
    book_item = session.query(models.Book).get(book_id)
    if not book_item:
        raise HTTPException(
            status_code=404, detail=f"Book with ID {book_id} not found"
        )
    session.delete(book_item)
    session.commit()
    session.close()
    return 'Book was deleted!'


app.include_router(api_router)
