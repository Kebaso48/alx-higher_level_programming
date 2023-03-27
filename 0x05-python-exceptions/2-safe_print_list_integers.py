#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print x elements of a list that are integers

    Args:
        my_list (list): list to print from
        x (int): number of elements to priny

    Return:
        number of elements printed
    """
    res = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            res += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (res)
