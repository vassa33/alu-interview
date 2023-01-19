#!/usr/bin/python3
import math
"""
The function minOperations calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    if n <= 0:
        return 0
    return int(math.log2(n)) + 1
