#!/usr/bin/python3
# 0-square.py by HendrixTech
"""A module that defines a square"""

class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size - represents the size of the square defined
        Raises:
            TypeError - if size is not an integer
            ValueError - if size is less than zero
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
