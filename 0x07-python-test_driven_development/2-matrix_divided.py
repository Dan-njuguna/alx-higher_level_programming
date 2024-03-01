#!/usr/bin/python3

def matrix_divided(matrix, div):
    new_matrix = []
    new_row = []
    if isinstance(matrix, list):
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        row1 = []
        for row in matrix:
            if len(row) > len(row1):
                row1 = row
                if len(row1) != len(row):
                    raise TypeError("Each row of the matrix must have the same size")
                for item in matrix:
                    if not isinstance(item, (int, float)):
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                    else:
                        res = item / div
                        new_row.append(res)
            new_matrix.append(new_row)
    return new_matrix
