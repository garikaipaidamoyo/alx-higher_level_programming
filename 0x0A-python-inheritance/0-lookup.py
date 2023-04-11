#!/usr/bin/python3
"""This module has returns the attributes and methods of object.
The module has the function lookup.
"""


def lookup(obj):
    """Function lookup().
    The lookup function return the attributes
    and methods of a given object.
    Args:i
        obj (obj): to be evaluated
    Returns:
        list of attributes and methods of object
    """
    return (dir(obj))
