#!/usr/bin/python3
"""DEfines a file apppending function"""


def append_write(filename="", text=""):
    """Appends string at end of a UTF8 file.

    Args:
        filename (str): name of file to append to
        text (str): the text to append
    Returns:
        number of characters appended
    """
    with open(filename, "a", encoding="utf-8")as f:
        return f.write(text)
