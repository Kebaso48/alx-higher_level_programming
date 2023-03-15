#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes all square values of integers of a matrix"""
    return ([list(map(lambda i: i * i, row)) for row in matrix])
