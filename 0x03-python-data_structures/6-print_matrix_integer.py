#!/usr/bin/python3

'''
'''


def print_matrix_integer(matrix=[[]]):
    for llist in matrix:
        for item in llist:
            if llist.index(item) == len(llist) - 1:
                print("{:d}".format(item))
            else:
                print("{:d}".format(item), end=" ")
