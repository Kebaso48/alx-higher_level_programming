#!/usr/bin/python3
def uniq_add(my_list=[]):
    """"add all unique integers of a list"""
    res = 0
    for i in set(my_list):
        res += i
    return (res)
