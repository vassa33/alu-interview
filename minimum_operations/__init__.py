"""
This module contains a function that calculates the fewest number of operations needed to result in exactly n H characters in the file.
The function can perform two operations: Copy All and Paste. It uses a greedy algorithm that repeatedly divides the target number n by 2 until it can no longer be divided.
The number of times it can be divided by 2 represents the number of "Copy All" operations needed, and the final number represents the number of "Paste" operations needed.

The module contains the following function:
    - min_operations : function that calculates the fewest number of operations needed to result in exactly n H characters in the file.

"""
