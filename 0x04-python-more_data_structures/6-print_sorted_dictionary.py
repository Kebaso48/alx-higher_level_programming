#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
    [print("{}: {}".format(n, a_dictionary[n])) for n in sorted(a_dictionary)]
