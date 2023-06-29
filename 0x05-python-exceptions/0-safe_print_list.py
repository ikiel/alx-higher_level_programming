#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    x = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            x += 1
            if my_list[i+1] is None:
                print()
    except IndexError:
        pass
    finally:
        return (x)
