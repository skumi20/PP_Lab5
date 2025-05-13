import pytest
import utils


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (4, 5, 9),
        (-1, 1, 0),
    ],
)
def test_add(a, b, expected):
    assert utils.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (4, 5, -1),
        (0, 0, 0),
    ],
)
def test_subtract(a, b, expected):
    assert utils.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (4, 5, 20),
        (0, 10, 0),
    ],
)
def test_multiply(a, b, expected):
    assert utils.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 2, 3.0),
        (5, 2, 2.5),
    ],
)
def test_divide(a, b, expected):
    assert utils.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        utils.divide(1, 0)
