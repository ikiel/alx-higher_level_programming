#!/usr/bin/python3

"""This module contains a funcion that writes to a file"""


def write_file(filename="", text=""):
    """This function writes text to a file an returns number of bytes written"""
    with open(filename, 'w', encoding='UTF8') as file:
        return file.write(text)
