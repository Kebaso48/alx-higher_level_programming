#!/usr/bin/python3
"""Defines a base model class"""


class Base:
    """Reps the base model

    Rpresents the “base” of all other classes in this project

    Attributes:
        __nb_objects (int): no of instaniated bases
    """
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base

        Args:
            id (int): identity of new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
