#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub ,mul, div
    from sys import argv
    import sys

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operators = {'+': add(a, b), '-': sub(a, b), '*': mul(a, b), '/': div(a, b)}
    operator = argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        print("{} {} {} = {}".format(a, argv[2], b, operators[operator]))
