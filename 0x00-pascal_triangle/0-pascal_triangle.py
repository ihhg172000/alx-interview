#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []
    for i in range(n):
        row = []
        for ii in range(i + 1):
            if ii == 0 or ii == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                row.append(prev_row[ii] + prev_row[ii - 1])
        triangle.append(row)
    return triangle
