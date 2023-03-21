#!/usr/bin/python3
"""
This function takes an integer n and returns
a list of lists of integers representing the
Pascal’s triangle of n.

Returns an empty list if n <= 0.
"""


def pascal_triangle(n):
    """    
    Arguments:
    n -- an integer representing the number
    of rows to generate
    
    Returns:
    A list of lists of integers representing 
    Pascal's triangle with n rows.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
