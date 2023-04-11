#!/usr/bin/python3
"""Defines a clas checking function"""


def is_same_class(obj, a_class):
    """checks if an object is same as instance of a given class.

    Args:
        obj (any): object to check
        a_class (type: the class to match obj type with
    Returns:
        True if obj is an exact of a_class, otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
