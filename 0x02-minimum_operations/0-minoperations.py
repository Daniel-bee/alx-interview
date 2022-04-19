#!/usr/bin/python3
"""
Minimum Operations
"""


def isPrime(num):
    """
    return True if the number is prime
    """
    flag = True
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break
    return flag


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n <= 0:
        return 0
    minOp = []
    for x in range(2, int((n / 2) + 1)):
        for y in range(1, int((n / 2) + 1)):
            pro, sum_ = (x * y), (x + y)
            if pro == n and sum_ not in minOp:
                minOp.append(sum_)
    if not minOp:
        return 0
    minOp.sort()
    return minOp[0]
