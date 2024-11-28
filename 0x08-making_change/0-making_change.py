#!/usr/bin/python3
"""
This module provides a function to determine the fewest number of coins
needed to meet a given total.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total.

    Args:
        coins (list): A list of the values of coins available.
        total (int): The total amount to achieve with the coins.

    Returns:
        int: The fewest number of coins needed, or -1 if it cannot be met.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0
    for coin in coins:
        if total <= 0:
            break
        coin_count += total // coin
        total %= coin

    if total != 0:
        return -1

    return coin_count
