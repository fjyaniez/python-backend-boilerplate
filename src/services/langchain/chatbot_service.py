import asyncio

from sqlmodel import Session

from functools import lru_cache
from typing import Type

from queue import Queue
from threading import Thread

from ...utils.config import Settings

from ...models.chatbot import Chatbot
from ...repositories.chatbot_repository import ChatbotRepository

from .chatbot_handler import ChatbotHandler

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage


class ChatbotService:
    def __init__(self, session: Session, settings: Settings, chatbot_key: str, streamer_queue: Queue) -> None:
        self._session = session
        self._settings = settings
        self._chatbot_key = chatbot_key
        self._streamer_queue = streamer_queue
        self._handler = ChatbotHandler(self._streamer_queue)

        if self._chatbot() is None:
            self.llm = None
        else:
            self.llm = ChatOpenAI(streaming=True, callbacks=[self._handler], model=self._chatbot().model,
                                  api_key=self._settings.openai_api_key)

    def chat(self, message: str) -> BaseMessage | None:
        if self.llm is None:
            return None

        return self.llm.invoke([
            SystemMessage(content=self._chatbot().system_prompt),
            HumanMessage(content=message)
        ])

    def start_generation(self, message: str):
        # Creating a thread with generate function as a target
        thread = Thread(target=self.chat, kwargs={"message": message})
        # Starting the thread
        thread.start()

    async def response_generator(self, message: str):
        # Start the generation process
        self.start_generation(message)

        # Starting an infinite loop
        while True:
            # Obtain the value from the streamer queue
            value = self._streamer_queue.get()
            # Check for the stop signal, which is None in our case
            if value is None:
                # If stop signal is found break the loop
                break
                # Else yield the value
            yield value
            # statement to signal the queue that task is done
            self._streamer_queue.task_done()

            # guard to make sure we are not extracting anything from
            # empty queue
            await asyncio.sleep(0.1)

    @lru_cache
    def _chatbot(self) -> Type[Chatbot] | None:
        return ChatbotRepository(self._session).get_by_key(self._chatbot_key)
