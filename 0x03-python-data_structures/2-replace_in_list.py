#!/usr/bin/python3

'''
 replace_in_list - replaces an element in a list
 @my_list: ...
 @idx: ...
 @element: ...
 Return: none if idx < 0, idx > len(my_list) and new list
'''


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return None

    for i in my_list:
        i_index = my_list.index(i)
        if i_index == idx:
            my_list[i_index] = element
            return my_list
