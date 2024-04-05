#!/usr/bin/python3
"""
0-validate_utf8.py
"""


def validUTF8(data):
    """
    Returns true if data is a valid utf-8 encoding else false.
    """
    in_sequence = 0

    for number in data:
        byte = number & 0b11111111

        if not in_sequence:
            if byte >> 7 == 0b00000000:
                continue

            if byte >> 3 == 0b00011110:
                in_sequence = 3
                continue

            if byte >> 4 == 0b00001110:
                in_sequence = 2
                continue

            if byte >> 5 == 0b00000110:
                in_sequence = 1
                continue

        if in_sequence and byte >> 6 == 0b00000010:
            in_sequence -= 1
            continue

        return False

    if in_sequence:
        return False

    return True
