import sys, os
sys.path.insert(0, os.path.abspath('./'))

from main import add, multiply


def test_add() -> None:
	assert add(1,2) == 3


def test_multiplication() -> None:
	assert multiply(2,2) == 4