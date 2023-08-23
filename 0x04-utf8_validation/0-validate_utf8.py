#!/usr/bin/python3
"""
utf-8 validation
"""


def validUTF8(data):
    """
    checks if the provided data is a valid utf8
    """

    if not data:
        return False

    for val in data:
        if (val >> 7) != 0:
            return False
    return True
