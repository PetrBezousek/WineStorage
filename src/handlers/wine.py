"""Handlers which perform CRUD operations with wine."""
from typing import NoReturn

from flask import abort, jsonify, request
from flask.views import MethodView
from httplib2 import Response

from src.config import EDIT_PASSWORD
from src.models import Wine, WineAdd, WineRemove, sqla


class WineHandler(MethodView):
    """/wine"""

    @staticmethod
    def post() -> NoReturn | Response:
        """Create a new wine. If a user is not authorized, abort with 403.

        Returns:
            NoReturn | Response: Response with wine's ID or 403 if a user is not authorized.
        """
        if request.args.get("heslo") != EDIT_PASSWORD:
            return abort(403)
        data = request.json
        wine = Wine(
            winery=data["winery"],
            variety=data["variety"],
            year=data["year"],
            attribute=data["attribute"],
            sugar=data["sugar"],
            count=data["count"],
        )
        sqla.session.add(wine)
        sqla.session.commit()
        for _ in range(wine.count):
            sqla.session.add(WineAdd(wine_id=wine.id))
        sqla.session.commit()
        return jsonify(wine_id=wine.id)


class WineIdHandler(MethodView):
    """/wine/<int:wine_id>"""

    @staticmethod
    def put(wine_id: int) -> NoReturn | Response:
        """Update a wine. If a user is not authorized, abort with 403.

        Args:
            wine_id (int): ID of the wine to update.

        Returns:
            NoReturn | Response: Response with wine's ID or 403 if a user is not authorized.
        """
        if request.args.get("heslo") != EDIT_PASSWORD:
            return abort(403)
        wine = Wine.query.filter_by(id=wine_id).one_or_none()
        if wine.count > request.json["count"]:
            for _ in range(wine.count - request.json["count"]):
                sqla.session.add(WineRemove(wine_id=wine_id))
        if wine.count < request.json["count"]:
            for _ in range(request.json["count"] - wine.count):
                sqla.session.add(WineAdd(wine_id=wine_id))

        wine.count = request.json["count"]

        sqla.session.commit()
        return jsonify(count=wine.count)

    @staticmethod
    def delete(wine_id: int) -> NoReturn | Response:
        """Archive a wine. Archived wine is not visible in the listing. If a user is not authorized, abort with 403.

        Returns:
            NoReturn | Response: Response with a deleted wine's ID or 403 if a user is not authorized.
        """
        if request.args.get("heslo") != EDIT_PASSWORD:
            return abort(403)
        wine = Wine.query.filter_by(id=wine_id).one_or_none()
        wine.is_archived = True
        sqla.session.commit()
        return jsonify(wine_id=wine_id)


class WineColumnAutocompleteHandler(MethodView):
    """/wine/<string:column>/autocomplete"""

    @staticmethod
    def get(column: str) -> Response:
        """Get non-archived wines' values for a column. Use result for auto-complete.

        Args:
            column (str): Database column name.

        Returns:
            Response: List of values for a column.
        """
        if hasattr(Wine, column):
            wine_columns = (
                Wine.query.filter(Wine.is_archived.is_(False))
                .with_entities(getattr(Wine, column))
                .group_by(getattr(Wine, column))
                .order_by(getattr(Wine, column).asc())
                .all()
            )
            return jsonify([str(getattr(x, column)) for x in wine_columns])
        return jsonify([])
