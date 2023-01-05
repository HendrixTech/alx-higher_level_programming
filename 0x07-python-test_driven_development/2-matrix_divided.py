#!/usr/bin/python3

"""
This is the "matrix_divided" module.
The module supplies one function, matrix_divided().
"""
def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    if type(matrix) != list or len(matrix) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for i in row:
            if type(i) != int and type(i) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    l = list(filter(lambda row: (len(row) == len(matrix[0])), matrix))
    if len(l) != len(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = [[round(x / div, 2) for x in row] for row in matrix]
    return new
