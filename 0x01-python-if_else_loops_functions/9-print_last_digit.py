#!/usr/bin/python3
'''
 print_last_digit - prints last digit of a number
 @number: number to print last digit for
 Return: value of last digit
'''


def print_last_digit(number):
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
