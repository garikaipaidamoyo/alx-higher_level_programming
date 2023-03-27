#!/usr/bash/python3
def safe_print_division(a, b):
    try:
        quotient = a / b
        print("Inside result:{}".format(quotient))
    except(ValueError, ZeroDivisionError):
        print("Inside result:None")
        quotient = None
    finally:
        return quotient 
