#!/usr/bin/python3

"""This module contains class Rectangle which inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """This class inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor for Rectangle"""
        super().__init__(id)

        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')

        self.width = width

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')

        self.height = height

        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')

        self.x = x

        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must >= 0')
        self.y = y

    @property
    def width(self):
        """A getter for width private attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """A setter for the width private attribute"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')

        self.__width = width

    @property
    def height(self):
        """A getter for the private attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """A  setter for the private attribute height"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')

        self.__height = height

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for the x attribute"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')

        self.__x = x

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y attribute"""
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must >= 0')
        self.__y = y

    def area(self):
        """Calculates the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """prints the Rectangle with # representation"""
        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            for _ in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """overide default __str__ method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Updates the class rectangle"""
        rec_attr = ['id', 'width', 'height', 'x', 'y']
        if (args):
            for i in range(len(args)):
                setattr(self, rec_attr[i], args[i])
        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])
