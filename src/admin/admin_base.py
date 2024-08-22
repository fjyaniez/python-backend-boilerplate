from sqladmin import Admin
from ..utils.db import Db

from .user_admin import UserAdmin

class AdminBase:
    admin = None

    def __init__(self, app):
        AdminBase.admin = Admin(app, Db.get_engine())

        AdminBase.admin.add_view(UserAdmin)
    