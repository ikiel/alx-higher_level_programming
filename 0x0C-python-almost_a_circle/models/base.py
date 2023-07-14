#!/usr/bin/python3

"""Contains the base class of the project"""


class Base:
    """This is the base class of the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        if id is None:
            __nb_objects += 1
            self.id = __nb_objects
