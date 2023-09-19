#!/usr/bin/python3
"""This module defines a rectangle that inherits from the Base class"""
from base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
                Args:
                    width (int): The width of the new Rectangle.
                    height (int): The height of the new Rectangle.
                    x (int): The x coordinate of the new Rectangle.
                    y (int): The y coordinate of the new Rectangle.
                    id (int): The identity of the new Rectangle.
                Raises:
                    TypeError: If either of width or height is not an int.
                    ValueError: If either of width or height <= 0.
                    TypeError: If either of x or y is not an int.
                    ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # List of getter functions
    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y

    # List of setter functions
    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the value for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Defines the rectangle using # """
        return self.__height * self.__width

    def display(self):
        """Prints the rectangle using #"""
        for y in range(self.y):
            print("")

        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Return the dictionary representations of a Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        Update the Rectangle.
                Args:
                    *args (ints): New attribute values.
                        - 1st argument represents id attribute
                        - 2nd argument represents width attribute
                        - 3rd argument represent height attribute
                        - 4th argument represents x attribute
                        - 5th argument represents y attribute
                    **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        obj_dictionary = {'id': self.id, 'width': self.__width,
                          'height': self.__height, 'x': self.__x,
                          'y': self.__y}

        return obj_dictionary