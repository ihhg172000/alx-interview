#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    h = 1
    selected_h = 0
    op = 0

    if n <= 0:
        return 0

    while n != h:
        if (n / h) % 1 == 0:
            op += 1
            selected_h = h

        op += 1
        h += selected_h

    return op
