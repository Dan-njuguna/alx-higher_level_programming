#!/usr/bin/python3
'''
 multiply_list_map - all values of list to be multiplied by number
 @my_list: a list of integers
 @number: multiply by
 Return: new list
'''


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
