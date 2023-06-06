#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    if n >= len(str):
        return str
    for i in range(len(str)):
        if i == n:
            continue
        else:
            s = s + str[i]
    return s
