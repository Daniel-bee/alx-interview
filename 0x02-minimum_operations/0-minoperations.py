#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    minOp = 0
    for x in range(2, (n + 1)):
        while n % x == 0:
            minOp += x
            n /= x
    return minOp
