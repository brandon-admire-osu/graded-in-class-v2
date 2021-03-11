from calc import *


def test_add():
    for a, b in enumerate(range(10)):
        assert add(a, b * 2) == a + b * 2


def test_sub():
    for a, b in enumerate(range(10)):
        assert sub(a, b * 2) == a - b * 2

