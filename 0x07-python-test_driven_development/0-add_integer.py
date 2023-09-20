#!/usr/bin/python3
"""
This module has just one function and it adds up two integers

"""

def add_integer(a, b=98):
    """
    Returns the sum of two integers or floats as integers

    Args:
        a: first integer
        b: second integer

    Returns:
        Sum of the two arguments

    Raises:
        TypeError: If either of the argument is not an integer or a float
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
