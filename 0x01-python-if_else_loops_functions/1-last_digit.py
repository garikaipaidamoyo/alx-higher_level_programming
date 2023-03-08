#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

a = number
b = number % 10
if b > 0:
    a = b % 10
else:
    a = abs(b) % 10
if b > 5:
    print("Last digit of {} is {} and is greater than 5".format(b, a))
elif a == 0:
    print("Last digit of {} is {} and is 0".format(b, a))
elif a < 6 and a != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(b, a))
