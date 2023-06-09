#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    c_list = sorted(my_list, reverse=True)
    return c_list[0]
