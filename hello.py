import random
import hashlib


def add(x, y):
    """This is an add function"""
    return x + y


def random_hash():
    """Generate a random SHA-256 has."""
    random_value = str(random.random())
    return hashlib.sha256(random_value.encode()).hexdigest()


if __name__ == "__main__":
    print(random_hash())
