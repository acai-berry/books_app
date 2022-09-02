from fastapi import FastAPI, APIRouter, HTTPException, status
from http import HTTPStatus

import app.models as models
from app.repository import Err, NO_OBJECT_ERROR
from app import controller


app = FastAPI()
api_router = APIRouter()


@api_router.get("/books/", tags=["books"], response_model=list[models.Book])
async def get_all_books():
    response = await controller.fetch_all_books()
    if type(response) == Err:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            detail="Server error, cannot handle the request.",
        )
    return response


@api_router.post(
    "/books/",
    tags=["books"],
    response_model=models.Book,
    status_code=status.HTTP_201_CREATED,
)
async def add_book(book: models.BookIn):
    response = await controller.add_book(book)
    if type(response) == Err:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            detail="Server error, cannot handle the request.",
        )
    return response


@api_router.get("/books/{book_id}", tags=["books"], response_model=models.Book)
async def get_book(book_id: int):
    response = await controller.fetch_a_book(book_id)
    if type(response) == Err and response.error == NO_OBJECT_ERROR:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value, detail="Book with such ID not found"
        )
    elif type(response) == Err:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            detail="Server error, cannot handle the request.",
        )
    return response


@api_router.put("/books/{book_id}", tags=["books"], response_model=models.Book)
async def update_book(book_id: int, book: models.BookIn):
    response = await controller.update_book(book_id, book)
    if type(response) == Err and response.error == NO_OBJECT_ERROR:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value, detail="Book with such ID not found"
        )
    elif type(response) == Err:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            detail="Server error, cannot handle the request.",
        )
    return response


@api_router.delete("/books/{book_id}", tags=["books"])
async def delete_book(book_id: int):
    response = await controller.delete_book(book_id)
    if type(response) == Err and response.error == NO_OBJECT_ERROR:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value, detail="Book with such ID not found"
        )
    elif type(response) == Err:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            detail="Server error, cannot handle the request.",
        )
    return response


@api_router.get("/health", tags=["health-check"])
async def health():
    return {"health": "It's working ✨"}


app.include_router(api_router)
