from flask import Flask
from flask_alembic import Alembic

from game_of_thrones.models import db
from game_of_thrones.apis import api_v1


def create_app():
    app = Flask(__name__)
    app.config.from_object('game_of_thrones.config.settings')

    db.init_app(app)
    api_v1.init_app(app)
    Alembic(app)

    return app
