from sqladmin import Admin

from ..utils.database import Database

from .chatbot_admin import ChatbotAdmin


class AdminBase:
    admin = None

    def __init__(self, app):
        AdminBase.admin = Admin(app, Database.get_engine())

        AdminBase.admin.add_view(ChatbotAdmin)
