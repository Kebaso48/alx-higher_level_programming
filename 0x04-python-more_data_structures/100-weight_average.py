#!/usr/bin/python3
def weight_average(my_list=[]):
    """wighted average of integers in a tuple"""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    mean = 0
    size = 0
    for tupl in my_list:
        mean += (tupl[0] * tupl[1])
        size += tupl[1]
    return (mean / size)
