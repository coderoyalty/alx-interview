#!/usr/bin/python3
"""
module contains function `makeChange`
"""


def makeChange(coins, total):
    """
    return fewest number of coin needed to meet `total`
    """
    remain = total
    n = len(coins)

    if total <= 0:
        return 0

    # sort coins into descending order
    # this way, the largest coin can be consumed first,
    # which minimizes for example having 2 twices instead 4.
    sorted_coins = sorted(coins, reverse=True)
    index = 0
    count = 0

    while remain > 0:
        if index >= n:
            return -1
        estimate = remain - sorted_coins[index]

        # remaining coin must be >= 0
        if estimate >= 0:
            remain -= sorted_coins[index]
            count += 1
        # if the possibility of becoming < 0 exists
        # increase your index
        else:
            index += 1

    return count
