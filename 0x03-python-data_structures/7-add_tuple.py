#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    elem_a = tuple_a + (0, 0)
    elem_b = tuple_b + (0, 0)

    new_tuple = (
            (elem_a[0] + elem_b[0]),
            (elem_a[1] + elem_b[1])
            )
    return new_tuple
