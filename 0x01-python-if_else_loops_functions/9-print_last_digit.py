#!/usr/bin/python3
def print_last_digit(number):
    """
    a function that prints the last digit
    """
    number = abs(number)
    last_digit = number % 10
    print(last_digit, end='')
    return last_digit
