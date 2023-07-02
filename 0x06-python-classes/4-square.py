#!/usr/bin/python3

"""define a square class to access and update private attribute"""


class Square:
    """square class with private size attribute and area"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @size.setter
    def size(self, value):
        """setter method for size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def size(self):
        """getter method for size"""
        return self.__size
