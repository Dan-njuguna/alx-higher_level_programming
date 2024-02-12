#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    if value in keys:
        del a_dictionary[value]
    else:
        return a_dictionary
    return a_dictionary