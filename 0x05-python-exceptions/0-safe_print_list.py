#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x lemnts of a list

    Args:
        my_list (list): list to print from
        x (int): number of elements to priny

    Return:
        number of elements printed
    """
    res = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            res += 1
        except IndexError:
            break
    print("")
    return (res)
