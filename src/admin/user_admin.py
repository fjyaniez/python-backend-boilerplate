from sqladmin import ModelView

from ..models.user import User

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name]    