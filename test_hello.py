from hello import add, random_hash
import hashlib


def test_add():
    assert 2 == add(1, 1)


def test_random_has():
    result = random_hash()

    assert isinstance(result, str)
    assert len(result) == 64
