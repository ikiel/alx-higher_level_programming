#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 or matrix is None:
        print()
    else:
        for row in matrix:
            for elem in row:
                print("{:d}".format(elem), end=" " if elem != row[-1] else "")
            print()
