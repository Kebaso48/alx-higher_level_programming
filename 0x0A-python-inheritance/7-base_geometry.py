#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


class BaseGeometry:
    """represents base geometry"""

    def area(self):
        """Not implementd"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates parameter as an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
