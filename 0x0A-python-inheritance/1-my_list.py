#!/usr/bin/python3
"""Defines an inherited list class MyList"""


class MyList(list):
    """Sorts a builtin list"""

    def print_sorted(self):
        """Prints a list in sorted ascending order"""
        print(sorted(self))
