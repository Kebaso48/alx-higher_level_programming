#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list"""
    multy = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multy.append(True)
        else:
            multy.append(False)

    return (multy)
