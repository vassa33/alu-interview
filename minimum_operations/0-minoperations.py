#!/usr/bin/python3
"""
The function minOperations calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


import math


def minOperations(n):
    if n <= 0:
        return 0
    operations = 0
    while n > 1:
        operations += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
    return operations
