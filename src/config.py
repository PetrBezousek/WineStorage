import os

from flask_env import MetaFlaskEnv

EDIT_PASSWORD = os.environ["EDIT_PASSWORD"]


class BaseConfig(metaclass=MetaFlaskEnv):
    """Base configuration for the app. Variables can be overriden with environment variables."""

    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Heroku provides a DATABASE_URL environment variable with `postgres` as a prefix.
    # There has to be a dialect + driver according to SQLAlchemy docs
    if os.environ["DATABASE_URL"].startswith("postgres://"):
        os.environ["DATABASE_URL"] = os.environ["DATABASE_URL"].replace("postgres", "postgresql+psycopg2", 1)

    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]


class DevelopmentConfig(BaseConfig):
    """Development configuration for the app. Variables can be overriden with environment variables."""

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(BaseConfig):
    """Production configuration for the app. Variables can be overriden with environment variables."""
