"""Database models for the application."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.ext.declarative import DeclarativeMeta

sqla = SQLAlchemy()
BaseModel: DeclarativeMeta = sqla.Model


class Wine(BaseModel):
    """Represents a bottle of wine."""

    __tablename__ = "wine"

    id = sqla.Column(sqla.Integer, primary_key=True)
    winery = sqla.Column(sqla.String(64))
    variety = sqla.Column(sqla.String(64))
    year = sqla.Column(sqla.Integer)
    attribute = sqla.Column(sqla.String(64))
    sugar = sqla.Column(sqla.String(64))
    count = sqla.Column(sqla.Integer, nullable=False, server_default=sqla.text("0"))
    is_archived = sqla.Column(sqla.Boolean, nullable=False, server_default=sqla.text("false"))


class WineAdd(BaseModel):
    """Time series of adding (buying) a bottle of wine."""

    __tablename__ = "wine_add"

    id = sqla.Column(sqla.Integer, primary_key=True)
    wine_id = sqla.Column(sqla.Integer, sqla.ForeignKey("wine.id"))
    time = sqla.Column(sqla.DateTime, server_default=func.now())


class WineRemove(BaseModel):
    """Time series of removing (drinking) a bottle of wine."""

    __tablename__ = "wine_remove"

    id = sqla.Column(sqla.Integer, primary_key=True)
    wine_id = sqla.Column(sqla.Integer, sqla.ForeignKey("wine.id"))
    time = sqla.Column(sqla.DateTime, server_default=func.now())
