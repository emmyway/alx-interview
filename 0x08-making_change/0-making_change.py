#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """ Determine the fewest coins needed to meet total amount """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins = total // coin  # Max number of this coin to use
        coin_count += num_coins
        total -= num_coins * coin

    if total != 0:
        return -1  # If the total cannot be met exactly
    return coin_count
