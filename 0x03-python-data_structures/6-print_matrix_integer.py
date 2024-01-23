#!/usr/bin/python3

'''
'''


def print_matrix_integer(matrix=[[]]):
    for llist in matrix:
        for item in llist:
            print("{:d}".format(item), end=" " if item != llist[-1] else "")
        print()
