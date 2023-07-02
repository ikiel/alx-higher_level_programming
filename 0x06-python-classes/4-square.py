#!/usr/bin/python3

"""create a square class"""


class Square:
    """square class with private size attribute and area"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def size(self, value):
        """setter method for size"""
        self.__size = value
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def size(self):
        """getter method for size"""
        return self.__size
