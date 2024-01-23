#!/usr/bin/python3

'''
 new_in_list - returns new list
 @my_list: older list
 @idx: index of element to replace
 @element: new element
 Return: new list
'''


def new_in_list(my_list, idx, element):
    new_list = []
    for item in my_list:
        new_list.append(item)

    if idx >= 0 and idx < len(new_list):
        new_list[idx] = element

    return (new_list)
