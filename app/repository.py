from app.database import database


class NotFoundError(Exception):
    pass


class SQLiteRepository:
    @staticmethod
    async def fetch_all(table):
        query = table.select()
        return await database.fetch_all(query)

    @staticmethod
    async def fetch_one(table, object_id):
        query = table.select().where(table.c.id == object_id)
        data = await database.fetch_one(query)
        if not data:
            return NotFoundError("No such object.")
        return data

    @staticmethod
    async def add_values(table, values):
        query = table.insert().values(values)
        record_id = await database.execute(query)
        query = table.select().where(table.c.id == record_id)
        data = await database.fetch_one(query)
        return data

    @staticmethod
    async def delete_object(table, object_id):
        query = table.delete().where(table.c.id == object_id)
        return await database.execute(query)

    @staticmethod
    async def update_values(table, updated_values, object_id):
        query = table.update().where(table.c.id == object_id).values(updated_values)
        await database.execute(query)
        query = table.select().where(table.c.id == object_id)
        data = await database.fetch_one(query)
        if not data:
            return NotFoundError("No such object.")
        return data
