"""Test sequence in factories."""


def test_id_not_zero(fctr_wine):
    assert fctr_wine().id != 0


def test_incremented_id(fctr_wine_add):
    assert fctr_wine_add().id == 1
    assert fctr_wine_add().id == 2
    assert fctr_wine_add().id == 3
