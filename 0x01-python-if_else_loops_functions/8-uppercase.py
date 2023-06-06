#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            s = chr(ord(c) - 32)
        else:
            s = c
        print("{}".format(s), end="")
    print()
