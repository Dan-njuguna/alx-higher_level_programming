#!/usr/bin/python3

'''
'''


def update_dictionary(a_dictionary, key, value):
    keys = []
    values = []
    for ikey in a_dictionary.keys():
        sorted(keys.append(ikey))
        if key in keys:
            a_dictionary[ikey] = value

        else:
            a_dictionary[key] = value
