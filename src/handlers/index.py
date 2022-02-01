"""Handlers for the index page."""
from flask import render_template, request
from flask.views import MethodView

from src.config import EDIT_PASSWORD
from src.models import Wine


class IndexHandler(MethodView):
    """/"""

    @staticmethod
    def get() -> str:
        """Get the index page which lists all wines.

        Returns:
            str: Rendered template.
        """
        token = request.args.get("heslo")
        wines = []
        wines_total_count = 0
        wines_type_count = 0

        for wine in Wine.query.filter(Wine.is_archived.is_(False)).all():
            wines_total_count += wine.count
            if wine.count > 0:
                wines_type_count += 1
            wines.append(
                {
                    "id": wine.id,
                    "winery": wine.winery,
                    "attribute": wine.attribute,
                    "variety": wine.variety,
                    "sugar": wine.sugar,
                    "year": wine.year,
                    "count": wine.count,
                }
            )

        wines = sorted(wines, key=lambda k: k["winery"], reverse=True)

        reordered_wines = []
        for wine in wines:
            if not wine["count"]:
                reordered_wines.append(wine)
            else:
                reordered_wines.insert(0, wine)

        return render_template(
            "index.html",
            wines=reordered_wines,
            token=token,
            authorized=token == EDIT_PASSWORD,
            wines_total_count=wines_total_count,
            wines_type_count=wines_type_count,
        )
