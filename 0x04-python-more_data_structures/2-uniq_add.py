#!/usr/bin/python3
'''
 uniq_add - adds all unique integers in a list
 @my_list: list to check
 Return: sum of uniques
'''


def uniq_add(my_list=[]):
    new = set(my_list)
    num = 0

    for i in new:
        num += i

    return num
