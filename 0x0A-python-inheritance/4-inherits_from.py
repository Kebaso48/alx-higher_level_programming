#!/usr/bin/python3
"""Defines an inherited class checking function"""


def inherits_from(obj, a_class):
    """checks if an object is an inherited instance of a clas.

    Args:
        obj (any): the object to check
        a_class (type): class to match type of obj to
    Returns:
        True if obj is an inherited instance, othrwis False
    """
    if issubclass(type(obj), a_class) and type(obj) !=a_class:
        return True
    return False
