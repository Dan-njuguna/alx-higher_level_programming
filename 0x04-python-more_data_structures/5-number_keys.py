#!/usr/bin/python3

'''
 number_keys - returms number of keys in a dictionary
 @a_dictionary: dictionary
 Return: number of keys
'''


def number_keys(a_dictionary):
    keys = []
    for item in a_dictionary.keys():
        keys.append(item)

    return len(keys)
