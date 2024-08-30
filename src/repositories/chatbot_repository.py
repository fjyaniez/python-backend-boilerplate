from sqlmodel import Session, select

from typing import Type

from ..models.chatbot import Chatbot


class ChatbotRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_key(self, _key: str) -> Type[Chatbot] | None:
        statement = select(Chatbot).where(Chatbot.key == _key)
        results = self.session.scalars(statement)

        return results.first()

    def create(self, chatbot: Chatbot) -> None:
        self.session.add(chatbot)
        self.session.commit()
