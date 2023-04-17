#!/usr/bin/python3
"""Defines a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square.

        Args:
            size (int): size of new square
            x (int): x axis of new square
            y (int): y axis of new square
            id (int): identity of new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """sets/gets size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """returns print() and str() rp of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.size)

    def update(self, *args, **kwargs):
        """Updates the square

        Args:
            *args (int): new attribute values
            -id is first argument
            -size is the second argument
            -x is the third argument
            -y is te fourth argument
            **kwargs (dict): new key/value pair
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for ke, val in kwargs.items():
                if ke == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif ke == "size":
                    self.size = val
                elif ke == "x":
                    self.x = val
                elif ke == "y":
                    self.y = val

    def to_dictionary(self):
        """Returns a dictionary representation of a square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }
