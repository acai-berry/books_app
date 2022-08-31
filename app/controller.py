from app.repository import SQLiteRepository
from app.database import books


async def fetch_all_books():
    return await SQLiteRepository.fetch_all(books)


async def add_book(book):
    values = {"title": book.title, "author": book.author, "price": book.price}
    return await SQLiteRepository.add_values(books, values)


async def fetch_a_book(book_id):
    return await SQLiteRepository.fetch_one(books, book_id)


async def update_book(book_id, book):
    updated_values = {"title": book.title, "author": book.author, "price": book.price}
    return await SQLiteRepository.update_values(books, updated_values, book_id)


async def delete_book(book_id):
    return await SQLiteRepository.delete_object(books, book_id)
