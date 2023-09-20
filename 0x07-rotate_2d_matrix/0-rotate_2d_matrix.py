#!/usr/bin/python3
"""
this module contains a
matrix rotation function
"""


def rotate_2d_matrix(matrix):
    """
    rotate NxN matrix
    """
    # transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            a = matrix[i][j]
            b = matrix[j][i]
            a, b = b, a
            matrix[i][j] = a
            matrix[j][i] = b
    # reverse each row
    for i in range(n):
        row = matrix[i]
        row = row[::-1]
        matrix[i] = row
    return
