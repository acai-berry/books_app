from sqlalchemy.exc import SQLAlchemyError
from dataclasses import dataclass
from app.database import database


@dataclass
class Err:
    error: str


NO_OBJECT_ERROR = "No such object!"


class SQLiteRepository:
    @staticmethod
    async def fetch_all(table):
        try:
            query = table.select()
            return await database.fetch_all(query)
        except SQLAlchemyError as err:
            return Err(str(err))

    @staticmethod
    async def fetch_one(table, object_id):
        try:
            query = table.select().where(table.c.id == object_id)
            data = await database.fetch_one(query)
            if not data:
                return Err(NO_OBJECT_ERROR)
            else:
                return data
        except SQLAlchemyError as err:
            return Err(str(err))

    @staticmethod
    async def add_values(table, values):
        try:
            query = table.insert().values(values)
            record_id = await database.execute(query)
            query = table.select().where(table.c.id == record_id)
            data = await database.fetch_one(query)
            return data
        except SQLAlchemyError as err:
            return Err(str(err))

    @staticmethod
    async def update_values(table, updated_values, object_id):
        try:
            query = table.update().where(table.c.id == object_id).values(updated_values)
            await database.execute(query)
            query = table.select().where(table.c.id == object_id)
            data = await database.fetch_one(query)
            if not data:
                return Err(NO_OBJECT_ERROR)
            else:
                return data
        except SQLAlchemyError as err:
            return Err(str(err))

    @staticmethod
    async def delete_object(table, object_id):
        try:
            query = table.select().where(table.c.id == object_id)
            data = await database.fetch_one(query)
            if not data:
                return Err(NO_OBJECT_ERROR)
            else:
                query = table.delete().where(table.c.id == object_id)
                return await database.execute(query)
        except SQLAlchemyError as err:
            return Err(str(err))
