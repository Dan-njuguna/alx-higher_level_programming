#!/usr/bin/python3

'''
 no_c - removes all characters c and C from a string
 @my_string: string to change
 Return: new string
'''


def no_c(my_string):
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            new_string = new_string + my_string[i]

    return new_string
