#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding.
    """
    flag = 1
    for num in data:
        if num <= -256 or num >= 256:
            flag = 0
            break
    if flag:
        return True
    return False
