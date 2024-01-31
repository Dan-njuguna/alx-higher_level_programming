#!/usr/bin/python3

'''
'''


def update_dictionary(a_dictionary, key, value):
    for ikey in sorted(a_dictionary.keys()):
        if ikey == key:
            a_dictionary[ikey] = value
        else:
            a_dictionary[key] = value

        print("{}: {}".format(ikey, a_dictionary[ikey]))
