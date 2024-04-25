#!/usr/bin/env python3
"""
0-rotate_2d_matrix.py
"""


def rotate_2d_matrix(matrix):
    """
    rotate_2d_matrix
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
