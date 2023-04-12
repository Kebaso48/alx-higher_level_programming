#!/usr/bin/python3
"""Defines a tsxt file inserting function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts text after each line containing a given string

    Args:
         filename (str): the file to append the string
         search_string (str): string to search for in the file
         new_string (str): string to insert 
    """
    txt = ""
    with open(filename) as r:
        for lin in r:
            txt += lin
            if search_string in lin:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
