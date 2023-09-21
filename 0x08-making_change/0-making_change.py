#!/usr/bin/python3
"""
module contains function `makeChange`
"""


def min_ignore_none(a, b):
    """
    an helper function that finds the min between `a` and `b`, except it
    returns b if a is None and vice versa
    """
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


def makeChange(coins, total):
    """
    return fewest number of coin needed to meet `total`
    """
    remain = total
    n = len(coins)

    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    index = 0
    count = 0

    while remain > 0:
        if index >= n:
            return -1
        estimate = remain - sorted_coins[index]

        if estimate >= 0:
            remain -= sorted_coins[index]
            count += 1
        else:
            index += 1

    return count
