import os

from flask_env import MetaFlaskEnv

EDIT_PASSWORD = os.environ["EDIT_PASSWORD"]


class BaseConfig(metaclass=MetaFlaskEnv):
    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Heroku hack TODO explain more
    if os.environ["DATABASE_URL"].startswith("postgres://"):
        os.environ["DATABASE_URL"] = os.environ["DATABASE_URL"].replace("postgres", "postgresql+psycopg2", 1)

    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(BaseConfig):
    pass
