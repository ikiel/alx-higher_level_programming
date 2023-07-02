#!/usr/bin/python3

"""
advanced task
"""

class MagicClass:
    """MagicClass"""
    def __init__(self, radius):
        """initialize radius"""
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')

        self.radius = radius

    def area(self):
        """calculate area of the circle"""
        from math import pi
        return (pi * (self.radius ** 2))

    def circumference(self):
        """calculate the circumference of the circle"""
        from math import pi
        return (2 * pi * self.radius)
