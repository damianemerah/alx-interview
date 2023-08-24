#!/usr/bin/python3
""" Making Change """
import sys


def makeChange(coins, total):
    """ Given a pile of coins of different values, determine the fewest number
        of coins needed to meet a given amount total """
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Compute the minimum number of coins for each amount from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if amount >= coin:
                min_coins[amount] = min(
                    min_coins[amount], min_coins[amount - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
