#!/usr/bin/python3
if __name__ == '__main__':
    import variable_load_5
    n = dir(variable_load_5)
    for i in range (0, len(n)):
        if n[i] == 'a':
            print(n[i])
