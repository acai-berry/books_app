from sqlalchemy import create_engine
from config import get_settings
import databases
import sqlalchemy

DATABASE_URL = get_settings().DATABASE


database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

books = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Float),
)


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)
