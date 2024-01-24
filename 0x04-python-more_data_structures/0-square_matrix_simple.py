#!/usr/bin/python3

'''
 square_matrix - computes value of all integers of a matrix.
 @matric: a 2D array
 Return: new matrix of squares of the elements of the older matrix
'''


def square_matrix_simple(matrix=[]):
    new_mat = matrix.copy()

    for i in range(len(matrix)):
        new_mat[i] = list(map(lambda x: x**2, matrix[i]))

    return new_mat
