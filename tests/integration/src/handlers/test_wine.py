import pytest

from src.handlers.wine import WineColumnAutocompleteHandler


@pytest.mark.parametrize("column", ["variety", "winery", "year", "attribute", "sugar", "unknown column"])
def test_autocomplete(snapshot, fctr_wine, column):
    fctr_wine()
    fctr_wine()
    snapshot.assert_match(WineColumnAutocompleteHandler.get(column).json)
