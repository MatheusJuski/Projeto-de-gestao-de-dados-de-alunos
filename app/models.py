from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Usuários hardcoded (em produção, use um banco de dados)
users = {
    1: User(1, 'admin', generate_password_hash('admin')),

}

@login.user_loader
def load_user(id):
    return users.get(int(id))