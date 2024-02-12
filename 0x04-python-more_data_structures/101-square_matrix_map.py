#!/usr/bin/python3

'''
 square_matrix_map - computes the square value of all integers of
    a matrix using map
 @matrix: a 2D array
 Return:
        Same size as matrix
        Each value should be the square of the value of the input
'''


def square_matrix_map(matrix=[]):
    if len(matrix) == 0:
        return 0
    new_matrix = list(map(lambda x: list(map((lambda y: (y**2)), x)), matrix))
    return new_matrix