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

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
