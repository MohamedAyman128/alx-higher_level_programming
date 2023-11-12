#!/usr/bin/python3
"""print_square

"""


def print_square(size):
    """print_square
    arg:
        size: size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
