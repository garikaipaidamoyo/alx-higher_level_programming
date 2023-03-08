#!/usr/bin/python3
def uppercase(str):
    """
    a function that prints a string in uppercase
    """
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - ord('a') + ord('A'))
        print(c, end='')
    print()
