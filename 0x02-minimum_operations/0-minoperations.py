#!/usr/bin/python3
"""
method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to
    get exactly n 'H' characters.
    
    Args:
    n (int): The target number of 'H' characters.
    
    Returns:
    int: Minimum number of operations to achieve exactly
    n 'H' characters. Returns 0 if n is not achievable.
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2

    # Factorize n and sum up the operations required
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
