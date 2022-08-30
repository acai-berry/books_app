from sqlalchemy.exc import SQLAlchemyError
from app.database import Base, engine, SessionLocal
from dataclasses import dataclass


# creates database
Base.metadata.create_all(engine)


@dataclass
class Err:
    error: str


NO_OBJECT_ERROR = "No such object!"


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
        except SQLAlchemyError as err:
            return Err(str(err))

    @staticmethod
    def fetch_one(object_id, session, model):
        try:
            data = session.query(model).get(object_id)
            if not data:
                return Err(NO_OBJECT_ERROR)
            else:
                return data
        except SQLAlchemyError as err:
            return Err(str(err))

    @staticmethod
    def _commit_changes(session):
        try:
            session.commit()
        except SQLAlchemyError as err:
            return Err(str(err))

    @staticmethod
    def add_object(session, object):
        try:
            session.add(object)
            SQLiteRepository._commit_changes(session)
            session.refresh(object)
        except SQLAlchemyError as err:
            return Err(str(err))

    @staticmethod
    def delete_object(object_id, model, session):
        try:
            object = SQLiteRepository.fetch_one(object_id, session, model)
            if type(object) == Err:
                return Err(NO_OBJECT_ERROR)
            session.delete(object)
            SQLiteRepository._commit_changes(session)
            session.close()
        except SQLAlchemyError as err:
            return Err(str(err))
