#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    n = dir()
    for i in range(0, len(n)):
        if n[i][0:2] != "__":
            print(n[i])
