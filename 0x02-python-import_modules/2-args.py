#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv) - 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        i = 1
        print(f"{n} arguments:")
        for arg in argv[1:]:
            print(f"{i}: {arg}")
            i += 1
