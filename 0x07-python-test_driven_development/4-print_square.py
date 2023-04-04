#!/usr/bin/python3
"""Defines a square printing function"""


def print_square(size):
    """prints a square

    Args:
        size (int): length/width of square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size <= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for s in range(size):
        [print("#", end="") for t in range(size)]
        print("")
