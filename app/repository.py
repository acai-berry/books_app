from app.database import database
from sqlalchemy.exc import SQLAlchemyError


class NotFoundError(Exception):
    pass


class DatabaseError(Exception):
    pass


class SQLiteRepository:
    @staticmethod
    async def fetch_all(table):
        try:
            query = table.select()
            data = await database.fetch_all(query)
            if not data:
                raise NotFoundError
            return data
        except NotFoundError:
            return NotFoundError("No records.")
        except SQLAlchemyError:
            return DatabaseError("Database error occured")

    @staticmethod
    async def fetch_one(table, object_id):
        try:
            query = table.select().where(table.c.id == object_id)
            data = await database.fetch_one(query)
            if not data:
                raise NotFoundError
            return data
        except NotFoundError:
            return NotFoundError("No such object.")
        except SQLAlchemyError:
            return DatabaseError("Database error occured")

    @staticmethod
    async def add_values(table, values):
        try:
            query = table.insert().values(values)
            response = await database.execute(query)
            return response
        except SQLAlchemyError:
            return DatabaseError("Database error occured")

    @staticmethod
    async def delete_object(table, object_id):
        try:
            query = table.delete().where(table.c.id == object_id)
            effected_rows = await database.execute(query)
            if effected_rows == 0:
                raise NotFoundError
        except NotFoundError:
            return NotFoundError("No such object.")
        except SQLAlchemyError:
            return DatabaseError("Database error occured")

    @staticmethod
    async def update_values(table, updated_values, object_id):
        try:
            query = table.update().where(table.c.id == object_id).values(updated_values)
            effected_rows = await database.execute(query)
            if effected_rows == 0:
                raise NotFoundError
        except NotFoundError:
            return NotFoundError("No such object.")
        except SQLAlchemyError:
            return DatabaseError("Database error occured")
