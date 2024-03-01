#!/usr/bin/python3

def matrix_divided(matrix, div):
    if isinstance(matrix, list):
        for row in matrix:
            for item in matrix:
                if not isinstance(item, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            