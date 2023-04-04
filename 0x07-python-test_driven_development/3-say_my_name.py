#!/usr/bin/python3
"""Defines a name printing function"""


def say_my_name(first_name, second_name=""):
    """Prints a name

    Args:
        first_name (str): first name to print
        second_name (str): second name to print
    Raises:
        TypeError: if neither name is a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(second_name, str):
        raise TypeError("second_name must be a string")
    print("My name is {} {}".format(first_name, second_name))
