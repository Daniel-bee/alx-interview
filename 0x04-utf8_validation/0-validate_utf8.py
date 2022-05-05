#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding.
    """
    count = 0
    for i, n in enumerate(data):
        byte = n & 0xFF
        if count:
            if byte >> 6 != 2:
                return False
            count -= 1
            continue
        while (1 << abs(7 - count)) & byte:
            count += 1
        if count == 1 or count > 4:
            return False
        count = max(count - 1, 0)
    return count == 0
