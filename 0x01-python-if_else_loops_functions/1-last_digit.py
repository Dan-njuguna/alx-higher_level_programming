#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number)
last_digit = num%10
if number > 0:
    last_digit = 1*last_digit
else:
    last_digit = -1*last_digit

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    pass
