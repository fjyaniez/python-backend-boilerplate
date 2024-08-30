from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine

from ..models.chatbot import Chatbot
from ..repositories.chatbot_repository import ChatbotRepository


class Database:
    engine = create_engine("sqlite:///database.db")

    @staticmethod
    def prepare() -> None:
        print("Preparing database...")
        Database.seed()

    @staticmethod
    def create_tables() -> None:
        SQLModel.metadata.create_all(Database.engine)

    @staticmethod
    def seed() -> None:
        session = Session(Database.get_engine())
        chatbot_repository = ChatbotRepository(session=session)

        if chatbot_repository.get_by_key("default") is None:
            chatbot = Chatbot(key="default", model="gpt-4o-mini", system_prompt="You are a helpful teacher.")
            chatbot_repository.create(chatbot)

    @staticmethod
    def get_engine() -> Engine:
        return Database.engine


def get_session() -> None:
    with Session(Database.get_engine()) as session:
        yield session
