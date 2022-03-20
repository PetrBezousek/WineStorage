from typing import Generator

import pytest
from pytest_factoryboy import register

from tests.factories import FctrWine, FctrWineAdd, FctrWineRemove

for factory in [FctrWine, FctrWineAdd, FctrWineRemove]:
    register(factory)

from flask import Flask

from src.config import IntegrationTestConfig
from src.flask_app import init_database
from src.models import sqla


@pytest.fixture(autouse=True, scope="session")
def app() -> Generator:
    """Application instance for the tests."""
    app = Flask(__name__)
    app.config.from_object(IntegrationTestConfig)

    with app.test_request_context():
        yield app


@pytest.fixture(autouse=True, scope="function")
def mock_sqla(app: Flask) -> None:
    """Connect to the PostgreSQL running in the local docker."""
    init_database(app)

    # Session teardown
    sqla.session.rollback()
    sqla.session.remove()
