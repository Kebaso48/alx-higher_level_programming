#!/usr/bin/python3

def safe_print_division(a, b):
    """divides  2 integers and print th result"""
    try:
        div = a / b
    except (TypeError,ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
