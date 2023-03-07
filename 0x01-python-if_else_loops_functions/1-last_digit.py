#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    Last_digit = number % 10
else:
    Last_digit = -((-number) % 10)
if Last_digit > 5:
    print("last digit is {:d} and is greater than 5".format(Last_digit))
elif Last_digit == 0:
    print("last digit is {:d} and is 0".format(Last_digit))
elif Last_digit < 6 and Last_digit != 0:
    print("last digit is {:d} and is less than 6 and not 0".format(Last_digit))
