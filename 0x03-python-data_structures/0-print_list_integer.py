#!/usr/bin/python3
'''
 print_list_integer - prints each integer in a list on a new line
 @my_list: a list of integers
 Return: Nothing
'''


def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
