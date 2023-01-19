#!/usr/bin/python3
"""
The function min_operations calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    if n <= 0:
        return 0
    copy_all = 0
    while n % 2 == 0:
        n = n // 2
        copy_all += 1
    return copy_all + n

