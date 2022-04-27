from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, user, password, tipoUser ="") -> None:
        self.id = id
        self.user = user
        self.password = password
        self.tipoUser = tipoUser

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

print(generate_password_hash("clavebelica1"))