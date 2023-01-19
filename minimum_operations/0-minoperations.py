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
        if n % 2 == 0:
            n = n // 2
        elif n % 3 == 0:
            n = n // 3
            operations += 2
        elif n % 5 == 0:
            n = n // 5
            operations += 4
        else:
            n -= 1
            operations += 1
    return operations
