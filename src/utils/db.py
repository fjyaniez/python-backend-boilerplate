from sqlmodel import Field, Session, SQLModel, create_engine

from ..models.user import User

class Db:
    engine = create_engine("sqlite:///database.db")

    @staticmethod
    def prepare():
        print("Preparing database...")
        SQLModel.metadata.create_all(Db.engine)

    @staticmethod
    def get_engine():
        return Db.engine