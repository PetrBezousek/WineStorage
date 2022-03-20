"""Classes for creating a mock of table rows."""
import factory

from src.models import Wine, WineAdd, WineRemove, sqla


class BaseFctr(factory.alchemy.SQLAlchemyModelFactory):
    """Base factory sets up the database session."""

    class Meta:
        sqlalchemy_session = sqla.session

    id = factory.Sequence(lambda n: n + 1)  # skip ID 0


class BaseFctrWineChange(BaseFctr):
    """Base factory for wine change tables with default data."""

    wine_id = factory.Sequence(lambda n: n + 1)  # skip ID 0
    time = "2020-01-01 00:00:00"


class FctrWine(BaseFctr):
    """Basic wine factory with default data."""

    class Meta:
        model = Wine

    winery = "winery"
    variety = "variety"
    year = 2020
    attribute = "attribute"
    sugar = "sugar"
    count = 1
    is_archived = False


class FctrWineAdd(BaseFctrWineChange):
    """Basic wine_add factory with default data."""

    class Meta:
        model = WineAdd


class FctrWineRemove(BaseFctrWineChange):
    """Basic wine_remove factory with default data."""

    class Meta:
        model = WineRemove
