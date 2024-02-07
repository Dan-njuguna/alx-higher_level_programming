#!/usr/bin/python3
'''
 simple_delete - deletes a key in a dectionary
 @a_dictionary: ...
 @key: the key
 Return: new dictionary
'''


def simple_delete(a_dictionary, key=""):
    dictionary = {}
    if key in a_dictionary.keys():
        del(a_dictionary[key])

    return a_dictionary
