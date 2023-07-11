#!/usr/bin/python3

"""This module appends text to a file"""


def append_write(filename="", text=""):
    """This function appends text to a file"""
    with open(filename, 'a', encoding="UTF8") as a_file:
        return a_file.write(text)
