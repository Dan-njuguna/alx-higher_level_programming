#!/usr/bin/python3

'''
 print_reversed_list_integer - reverses a list of integers
 @my_list: a list of integers
 Return: Nothing
'''


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return

    llist = len(my_list) - 1
    for i in range(llist, -1, -1):
        print("{}".format(my_list[i]))
