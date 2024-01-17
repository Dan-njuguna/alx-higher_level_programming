#!/usr/bin/python3
'''
 islower: checks is a given character if lowercase or uppercase
 @c: character to check if lowercase
 Return: True if c is lowercase and False if otherwise
'''

def islower(c):
    for num in range(97, 123):
        if ord(c) == num:
            return True
        else:
            return False
