#!/usr/bin/python3

"""This module contains a function read_file"""


def read_file(filename=""):
    """This fuction reads a file and prints to stdout"""
    with open(filename, 'r', encoding="UTF8") as the_file:
        content = the_file.read()
    print(content, end="")
