#!/usr/bin/python3

'''
 only_diff_elements - returns a list of different elements in two sets.
 @set_1: first set element
 @set_2: secind set element
 Return: List of different elements of the sets
'''


def only_diff_elements(set_1, set_2):
    uniq = []
    uniq1 = []
    for item in set_1:
        if item not in set_2:
            uniq.append(item)
    for item in set_2:
        if item not in set_1:
            uniq.append(item)

    return uniq
