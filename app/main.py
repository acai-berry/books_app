from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from http import HTTPStatus

import app.schemas as schemas
from app.repository import get_session
from app.controller import SQLiteController


app = FastAPI()
api_router = APIRouter()


@api_router.get("/books/", tags=["books"])
def get_all_books(session: Session = Depends(get_session)):
    books = SQLiteController.fetch_all_books(session)
    if books == Exception:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND.value)
    return books


@api_router.post("/books/", tags=["books"])
def add_book(book: schemas.Book, session: Session = Depends(get_session)):
    return SQLiteController.add_book(book, session)


@api_router.get("/books/{book_id}", tags=["books"])
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = SQLiteController.fetch_a_book(book_id, session)
    if book == Exception:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND.value)
    return book


@api_router.put("/books/{book_id}", tags=["books"])
def update_book(
    book_id: int, book: schemas.Book, session: Session = Depends(get_session)
):
    return SQLiteController.update_book(book_id, book, session)


@api_router.delete("/books/{book_id}", tags=["books"])
def delete_book(book_id: int, session: Session = Depends(get_session)):
    book = SQLiteController.delete_book(book_id, session)
    if book == Exception:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND.value)
    return book


@api_router.get("/health", tags=["health-check"])
def health():
    return {"health": "It's working ✨"}


app.include_router(api_router)
