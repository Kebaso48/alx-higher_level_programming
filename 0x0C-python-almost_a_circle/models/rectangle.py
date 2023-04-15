#!/usr/bin/python3
"""Defines a clas rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializws a new rctangle

        Args:
            width (int): width of new rectangle
            height (int): height of new rect
            x (int): x axis of nw rect
            y (int): y axis of new rect
            id (int): identity of new rect
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Sets/Gets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Sets?gets height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """sets/gets x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """sets/gets y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area"""
        return self.width * self.height

    def display(self):
        """displays rectangle with'#' character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for hei in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wi in range(self.width)]
            print("")

    def __str__(self):
        """returns print() and str() representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height)
