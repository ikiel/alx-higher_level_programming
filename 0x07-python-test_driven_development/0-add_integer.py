#!/usr/bin/python3
"""
A function that adds two integers a and b
"""

def add_integer(a, b=98):
    """adds two integers"""
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) is float or type(b) is float:
        a, b = int(a), int(b)

    return (a + b)
