from sqlalchemy.exc import SQLAlchemyError
from app.database import Base, engine, SessionLocal

# creates database
Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


class SQLiteRepository:
    @staticmethod
    def fetch_all(model, session):
        try:
            data = session.query(model).all()
            return data
        except SQLAlchemyError:
            return Exception

    @staticmethod
    def fetch_one(object_id, session, model):
        data = session.query(model).get(object_id)
        if not data:
            return Exception
        else:
            return data

    @staticmethod
    def add_object(session, object):
        session.add(object)
        session.commit()
        session.refresh(object)

    @staticmethod
    def delete_object(object_id, model, session):
        object = SQLiteRepository.fetch_one(object_id, session, model)
        if object == Exception:
            return object
        session.delete(object)
        session.commit()
        session.close()
