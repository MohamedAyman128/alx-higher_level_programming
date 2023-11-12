#!/usr/bin/python3
"""add_integer

"""


def add_integer(a, b=98):
    """add_integer
    arg:
        a: integer number
        b: integer number
    """
    if not isinstance(a, (int, float)):
        raise TypeError ("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError ("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b) 
       
    return a + b
