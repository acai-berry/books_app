from fastapi import HTTPException


class SQLiteRepository:
    @staticmethod
    def get_all(model, session):
        docs = session.query(model).all()
        return docs

    @staticmethod
    def get_one(object_id, session, model):
        object = session.query(model).get(object_id)
        if not object:
            raise HTTPException(
                status_code=404, detail=f"Object with ID {object_id} not found"
            )
        return object

    @staticmethod
    def add_object(session, object):
        session.add(object)
        session.commit()
        session.refresh(object)

    @staticmethod
    def delete_object(object_id, model, session):
        object = SQLiteRepository.get_one(object_id, session, model)
        session.delete(object)
        session.commit()
        session.close()
        return "Object was deleted!"
