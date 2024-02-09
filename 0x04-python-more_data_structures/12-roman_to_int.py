#!/usr/bin/python3

'''
 roman_to_int - converts a Roman numeal to an integer
 @roman_string: Sting of Roman Numeral
 Return: 0 if roman_string is not a string of None, otherwise integer
'''


def roman_to_int(roman_string):
    if roman_string is None or roman_string is not type("Roman String"):
        return 0

    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev = 0
    for i in roman_string:
        val = roman_d[i]
        if val > prev:
            num += val - 2 * prev
        else:
            num += val
        prev = val

    return num
