#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 or matrix is None:
        print()
    else:
        for row in matrix:
            for elem in row:
                if (row.index(elem)) == (len(row) - 1):
                    print("{:d}".format(elem))
                else:
                    print("{:d}".format(elem), end=" ")
