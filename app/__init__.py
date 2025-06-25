from flask import Flask
from config import Config
from app.extensions import login
from app.routes import init_routes, atualizar_cache_threaded

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login.init_app(app)
    login.login_view = 'login'

    init_routes(app)

    with app.app_context():
        atualizar_cache_threaded(app)

    return app

