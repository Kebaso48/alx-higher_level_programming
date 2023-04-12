#!/usr/bin//python3
"""Defines a text-reading file function"""


def read_file(filename=""):
    """prints contenets of UTF8 file to std out"""
    with open(filename, encoding="utf-8")as f:
        print(f.read(), end="")
