#!/usr/bin/python3
"""
0-validate_utf8.py
"""


def utf8_control_bits(byte):
    """
    Returns utf-8 control bits.
    """
    control_bits = 1

    while byte & 0b10000000:
        if control_bits == 5:
            return 0

        control_bits += 1
        byte = byte << 1

    return control_bits


def validUTF8(data):
    """
    Returns true if data is a valid utf-8 encoding else false.
    """
    for byte_idx in range(len(data)):
        sequence = utf8_control_bits(data[byte_idx]) - 1

        if sequence == -1:
            return False

        for _ in range(sequence):
            byte_idx += 1

            if utf8_control_bits(data[byte_idx]) != 2:
                return False

    return True
