#!/usr/bin/python3
"""
0-validate_utf8.py
"""


def validUTF8(data):
    """
    Returns true if data is a valid utf-8 encoding else false.
    """
    in_sequence = 0

    for byte in data:
        if not in_sequence and byte >> 7 == 0b00000000:
            continue

        if not in_sequence and byte >> 3 == 0b00011110:
            in_sequence = 3
            continue

        if not in_sequence and byte >> 4 == 0b00001110:
            in_sequence = 2
            continue

        if not in_sequence and byte >> 5 == 0b00000110:
            in_sequence = 1
            continue

        if in_sequence and byte >> 6 == 0b00000010:
            in_sequence -= 1
            continue

        return False

    return True