#!/usr/bin/python3
"""Defines a class and inherited class checking function"""


def is_kind_of_class(obj, a_class):
    """Chck if an object is an instance or inherited instance of a clas.

    Args:
        obj (any):object to check
        a_class (type):  class to match obj yo
    Returns:
        True if obj is instance or inherited instance of a_class
        False if otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
