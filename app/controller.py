from app.repository import SQLiteRepository
import app.models as models
import app.schemas as schemas


def fetch_all_books(session):
    return SQLiteRepository.fetch_all(models.Book, session)


def fetch_a_book(book_id, session):
    return SQLiteRepository.fetch_one(book_id, session, models.Book)


def add_book(book: schemas.Book, session):
    book = models.Book(title=book.title, author=book.author, price=book.price)
    SQLiteRepository.add_object(session, book)
    return book


def update_book(book_id: int, book: schemas.Book, session):
    book_updated = SQLiteRepository.fetch_one(book_id, session, models.Book)
    book_updated.title = book.title
    book_updated.author = book.author
    book_updated.price = book.price
    SQLiteRepository._commit_changes(session)
    return book_updated


def delete_book(book_id: int, session):
    return SQLiteRepository.delete_object(book_id, models.Book, session)
