import pytest
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (1.5, 2.5, 4.0),
        (-1, -2, -3),
        (0, 0, 0),
    ]
)

def test_add(a, b, expected):
    from calc.ops import add
    assert add(a, b) == expected