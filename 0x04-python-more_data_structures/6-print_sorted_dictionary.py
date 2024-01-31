#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dict = {}
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))

