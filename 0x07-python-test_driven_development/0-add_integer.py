#!/usr/bin/python3
"""Defines integer addition function"""


def add_integer(a, b=98):
    """Function that adds two integers
    floats are typecast into intgrs before addition

    Raises:
        TypeError if neither a nor b is an integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
