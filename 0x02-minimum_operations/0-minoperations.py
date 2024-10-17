#!/usr/bin/python3
"""
Module that provides a function to calculate the minimum operations
to get exactly n 'H' characters using only 'Copy All' and 'Paste'.
"""

def minOperations(n):
    """Calculates the minimum number of operations to achieve n 'H' characters."""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Factor n by dividing it with the smallest possible prime numbers
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

