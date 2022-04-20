#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if type(n) not in [int]:
        return 0
    minOp = 0
    for x in range(2, n):
        while n % x == 0:
            minOp += x
            n /= x
    return minOp
