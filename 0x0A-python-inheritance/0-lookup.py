#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj):
    """Returns lists of attributes and methods of an object"""
    return (dir(obj))
