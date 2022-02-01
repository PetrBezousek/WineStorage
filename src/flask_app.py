"""Module for creating the flask app"""
import os
from pathlib import Path

from flask import Flask
from flask_migrate import Migrate, upgrade

from src.config import DevelopmentConfig, ProductionConfig
from src.handlers.index import IndexHandler
from src.handlers.wine import WineColumnAutocompleteHandler, WineHandler, WineIdHandler
from src.models import sqla


def create_app() -> Flask:
    """Create the flask app"""
    app = Flask(__name__)

    if os.environ.get("FLASK_ENV") == "development":
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)

    init_database(app)
    init_url_rules(app)
    return app


def init_url_rules(app: Flask) -> None:
    """Init all URL rules

    Args:
        app (Flask): Flask app
    """
    app.add_url_rule("/wine/<int:wine_id>", view_func=WineIdHandler.as_view("wine_id"))
    app.add_url_rule("/wine", view_func=WineHandler.as_view("wine"))
    app.add_url_rule("/", view_func=IndexHandler.as_view("index"))
    app.add_url_rule(
        "/wine/<string:column>/autocomplete",
        view_func=WineColumnAutocompleteHandler.as_view("wine_autocomplete"),
    )


def init_database(app) -> None:
    """Init the database and run Alembic migrations"""
    sqla.init_app(app)

    Migrate(app, sqla)
    with app.app_context():
        upgrade(directory=f"{Path(__file__).parent}/migrations", revision="head")
