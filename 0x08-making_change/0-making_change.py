#!/usr/bin/python3
""" Making Change """
import sys


def makeChange(coins, total):
    """ Given a pile of coins of different values, determine the fewest number
        of coins needed to meet a given amount total """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    print(coins)
    count = 0
    for coin in coins:
        if coin <= total:
            count += total // coin
            total = total % coin
        if total == 0:
            break
    if total != 0:
        return -1
    return count


print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
