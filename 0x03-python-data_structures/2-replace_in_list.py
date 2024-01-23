#!/usr/bin/python3

'''
 replace_in_list - replaces an element in a list
 @my_list: ...
 @idx: ...
 @element: ...
 Return: none if idx < 0, idx > len(my_list) and new list
'''


def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list
