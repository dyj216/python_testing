import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize(
    "fn_input,expected",
    [
        (4, 2),
        (9, 3),
        (16, 4),
    ]
)
def test_square_root(calc, fn_input, expected):
    assert expected == calc.square_root(fn_input)
