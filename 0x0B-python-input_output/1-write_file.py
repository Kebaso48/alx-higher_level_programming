#!/usr/bin/python3
"""Defines a file writing function"""


def write_file(filename="", text=""):
    """writes a string to a utf-8 text fil.

    Args:
        filename (str): the name of file
        text (str): text to write to file
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
