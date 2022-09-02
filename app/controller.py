from app.database import books


async def fetch_all_books(repository):
    return await repository.fetch_all(books)


async def add_book(repository, book):
    values = {"title": book.title, "author": book.author, "price": book.price}
    return await repository.add_values(books, values)


async def fetch_a_book(repository, book_id):
    return await repository.fetch_one(books, book_id)


async def update_book(repository, book_id, book):
    updated_values = {"title": book.title, "author": book.author, "price": book.price}
    return await repository.update_values(books, updated_values, book_id)


async def delete_book(repository, book_id):
    return await repository.delete_object(books, book_id)
