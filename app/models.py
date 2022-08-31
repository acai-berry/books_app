from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float


class BookIn(BaseModel):
    title: str
    author: str
    price: float
