from fastapi import HTTPException, status, APIRouter
from http import HTTPStatus

import app.models as models
from app.repository import SQLiteRepository, NotFoundError
from app import controller

api_router = APIRouter()


@api_router.get("/books/", tags=["books"], response_model=list[models.Book])
async def get_all_books():
    response = await controller.fetch_all_books(SQLiteRepository)
    if isinstance(response, NotFoundError):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value, detail="No books available."
        )
    return response


@api_router.post(
    "/books/",
    tags=["books"],
    response_model=models.Book,
    status_code=status.HTTP_201_CREATED,
)
async def add_book(book: models.BookIn):
    response = await controller.add_book(SQLiteRepository, book)
    return response


@api_router.get("/books/{book_id}", tags=["books"], response_model=models.Book)
async def get_book(book_id: int):
    response = await controller.fetch_a_book(SQLiteRepository, book_id)
    if isinstance(response, NotFoundError):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value, detail="Book with such ID not found"
        )
    return response


@api_router.delete("/books/{book_id}", tags=["books"])
async def delete_book(book_id: int):
    response = await controller.delete_book(SQLiteRepository, book_id)
    if isinstance(response, NotFoundError):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value, detail="Book with such ID not found"
        )
    return {"detail": "Successfully deleted!"}


@api_router.put("/books/{book_id}", tags=["books"], response_model=models.Book)
async def update_book(book_id: int, book: models.BookIn):
    response = await controller.update_book(SQLiteRepository, book_id, book)
    if isinstance(response, NotFoundError):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value, detail="Book with such ID not found"
        )
    return response
