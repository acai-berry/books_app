from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from http import HTTPStatus

import app.schemas as schemas
from app.repository import get_session, Err, NO_OBJECT_ERROR
from app import controller


app = FastAPI()
api_router = APIRouter()


@api_router.get("/books/", tags=["books"])
def get_all_books(session: Session = Depends(get_session)):
    response = controller.fetch_all_books(session)
    if type(response) == Err:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value)
    return response


@api_router.post("/books/", tags=["books"])
def add_book(book: schemas.Book, session: Session = Depends(get_session)):
    response = controller.add_book(book, session)
    if type(response) == Err:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value)
    return response


@api_router.get("/books/{book_id}", tags=["books"])
def get_book(book_id: int, session: Session = Depends(get_session)):
    response = controller.fetch_a_book(book_id, session)
    if type(response) == Err and response.error == NO_OBJECT_ERROR:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND.value)
    elif type(response) == Err:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value)
    return response


@api_router.put("/books/{book_id}", tags=["books"])
def update_book(
    book_id: int, book: schemas.Book, session: Session = Depends(get_session)
):
    response = controller.update_book(book_id, book, session)
    if type(response) == Err and response.error == NO_OBJECT_ERROR:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND.value)
    elif type(response) == Err:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value)
    return response


@api_router.delete("/books/{book_id}", tags=["books"])
def delete_book(book_id: int, session: Session = Depends(get_session)):
    response = controller.delete_book(book_id, session)
    if type(response) == Err and response.error == NO_OBJECT_ERROR:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND.value)
    elif type(response) == Err:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value)
    return response


@api_router.get("/health", tags=["health-check"])
def health():
    return {"health": "It's working ✨"}


app.include_router(api_router)
