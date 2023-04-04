#!/usr/bin/python3
"""
The program that prints a square with the character #
"""
def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("ize must be an integer")

    for i in range(0, size):
        print("#" * size)
