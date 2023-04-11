#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of the available attributes and methods of an object.
    """
    result = []
    for attr_name in dir(obj):
        if not attr_name.startswith('_'):
            result.append(attr_name)
    return result
