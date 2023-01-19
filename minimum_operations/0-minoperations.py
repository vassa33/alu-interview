#!/usr/bin/python3

def minOperations(n):

    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.
    The function can perform two operations: Copy All and Paste.
    The function uses a greedy algorithm that repeatedly divides the target number n by 2 until it can no longer be divided. 
    The number of times it can be divided by 2 represents the number of "Copy All" operations needed, 
    and the final number represents the number of "Paste" operations needed.
    """
    
    if n <= 0: 
        return 0
    else:
        copy_all = 0
        while n % 2 == 0:
            n = n // 2
            copy_all += 1
        return copy_all + (n - 1)
