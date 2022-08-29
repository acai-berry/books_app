from fastapi import HTTPException


class SQLiteRepository:
    def get_all(self, model, session):
        docs = session.query(model).all()
        return docs

    def get_one(self, object_id, session, model):
        object = session.query(model).get(object_id)
        if not object:
            raise HTTPException(
                status_code=404, detail=f"Object with ID {object_id} not found"
            )
        return object

    def add_object(self, session, object):
        session.add(object)
        session.commit()
        session.refresh(object)

    def delete_object(self, object_id, model, session):
        object = self.get_one(object_id, session, model)
        session.delete(object)
        session.commit()
        session.close()
        return "Object was deleted!"
