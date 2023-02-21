#!/usr/bin/python3
"""Rain. """


def rain(walls):
    """
    Calculates the amount of water retained between walls after it rains.

    Args:
    walls: A list of non-negative integers representing the heights of walls
    with unit width 1, as if viewing the cross-section of a relief map.

    Returns:
    An integer indicating the total amount of rainwater retained between the walls.

    Assumes that the ends of the list (before index 0 and after index walls[-1])
    are not walls, meaning they will not retain water.
    If the list is empty, returns 0.
    """
    n = len(walls)
    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])

    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - walls[i]

    return water if water >= 0 else 0
