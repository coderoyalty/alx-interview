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
    if total <= 0:
        return 0
    cache = {}

    cache[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            sub = i - coin
            if sub < 0:
                continue
            if cache.get(sub) is None:
                return -1
            else:
                cache[i] = min_ignore_none(cache.get(i), cache.get(sub) + 1)

    return cache[total]
