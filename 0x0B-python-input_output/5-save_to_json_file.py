#!/usr/bin/python3

"""This module writes JSON to a text file"""

import json
"""json module that provides json functionalities"""


def save_to_json_file(my_obj, filename):
    """converts object to JSON and writes to file"""
    with open(filename, 'w', encoding="UTF8") as a_file:
        json.dump(my_obj, a_file)
