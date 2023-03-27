#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): integer to print

    Return:
        if ValueError or TypeError occurs - False
        else - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
