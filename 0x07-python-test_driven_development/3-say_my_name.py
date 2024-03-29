#!/usr/bin/python3
"""
The program that prints My name is <first name> <last name>
"""

def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if len(last_name) > 0:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))   
