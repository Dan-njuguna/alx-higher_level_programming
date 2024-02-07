#!/usr/bin/python3
'''
 multiply_by_2 - returns a new dictionary with all the values multiplied by 2
 @a_dictionary: ...
 Return: ...
'''


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    values = []
    for key in sorted(new_dict.keys()):
        new_dict[key] *= 2

    return new_dict
