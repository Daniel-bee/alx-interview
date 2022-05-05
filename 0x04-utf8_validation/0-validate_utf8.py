#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding.
    """
    count = 0
    for char in data:
        if (char & 255) == 0:
            return False
        if count == 0:
            if (char >> 5) == 0b110:
                count = 1
            elif (char >> 4) == 0b1110:
                count = 2
            elif (char >> 3) == 0b11110:
                count = 3
            elif (char >> 7):
                return False
        else:
            if (char >> 6) != 0b10:
                return False
            count -= 1
    return True
