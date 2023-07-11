#!/usr/bin/python3

"""This module contains a function that handles JSON and strings"""
import json
"""json module"""


def to_json_string(my_obj):
    """returns JSON representation of a string"""
    return json.dumps(my_obj)
