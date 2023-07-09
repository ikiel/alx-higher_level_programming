#!/usr/bin/python3
"""
A function that divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    new_matrix =[]
    list_error = "matrix must be a matrix (list of lists) of integeres or floats"

    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(list_error)
    if type(div) in [int, float, None]
        pass
    else:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if matrix[0]:
        length = len(matrix[0])
    else:
        raise TypeError(list_error)

    for i in range(len(matrix)):
        if len(matrix[i]) == length:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for n in matrix[i]:
            if type(n) in [int, float]:
                new_matrix[i].append(round(n / div, 2))
            else:
                raise TypeError(error)
    return new_matrix
