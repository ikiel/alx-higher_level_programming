#!/usr/bin/python3

"""This module contains a function read_file"""


def read_file(filename=""):
    with open(filename, 'r', encoding="UTF8") as the_file:
        for line in the_file:
            print(line)
