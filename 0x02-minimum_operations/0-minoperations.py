#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    calculate the minimum operations
    """
    number = n
    div = 2
    cnt = 0

    while (number > 1):
        if number % div == 0:
            number = int(number / div)
            cnt += div
            div = 2
        else:
            div += 1

    return cnt
