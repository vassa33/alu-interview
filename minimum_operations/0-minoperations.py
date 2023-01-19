#!/usr/bin/python3
"""
The function min_operations calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""

def min_operations(n):
    if n <= 0:
        return 0
    else:
        binary_n = bin(n)[2:]
        trailing_zeroes = len(binary_n) - len(binary_n.rstrip('0'))
        return len(binary_n) - trailing_zeroes
