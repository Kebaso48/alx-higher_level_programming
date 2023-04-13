#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Represents a students"""

    def __init__(self, first_name, last_name, age):
        """Initialize a nw student

        Args:
            first_name (str): first name of student
            last_name (str): second name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        if attrs is a list of strings it represents  only attriutes
        included in the list

        Args:
            attrs (list): (optional) attributs to represent
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
