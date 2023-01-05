#!/usr/bin/python3

"""
module - add integer.

Takes two arguments and return the sum.
"""

def add_integer(a, b=98):
    """
    add_integer
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integeer')

    return int(a) + int(b)
