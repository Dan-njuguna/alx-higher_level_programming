#!/usr/bin/python3
'''
 uppercase - prints a string in uppercase followed by a newline.
 @str: string to convert to uppercase
 Return: nothing
'''


def uppercase(str):
    for i in str:
        if ord(i) >= 90 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
