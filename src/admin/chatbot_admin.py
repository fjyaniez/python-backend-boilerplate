from sqladmin import ModelView

from ..models.chatbot import Chatbot


class ChatbotAdmin(ModelView, model=Chatbot):
    column_list = [Chatbot.key, Chatbot.model]
