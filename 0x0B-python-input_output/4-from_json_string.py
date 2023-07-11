#!/usr/bin/python3

"""This module converts python object to JSON representation"""

import json
"""json module"""


def from_json_string(my_str):
    """converts python object to JSON representation"""
    return json.loads(my_str)
