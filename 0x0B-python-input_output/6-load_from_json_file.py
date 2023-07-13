#!/usr/bin/python3

"""This module creates a python object from a JSON file"""

import json
"""json module with all the json functionalities"""


def load_from_json_file(filename):
    """create an object from a json file"""
    with open(filename, 'r', encoding="UTF8") as a_file:
        json.load(a_file)
