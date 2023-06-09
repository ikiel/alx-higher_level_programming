#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for word in my_string:
        if word in "cC":
            continue
        else:
            s += word
    return s
