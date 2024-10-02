#!/usr/bin/python3
"""
Prime Game
"""

def sieve_of_eratosthenes(n):
    """ Returns a list of primes up to n using the Sieve of Eratosthenes """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(n + 1) if sieve[i]]


def isWinner(x, nums):
    """ Determine the winner after x rounds of the Prime Game """
    if not nums or x < 1:
        return None

    # Precompute prime numbers up to the maximum value in nums
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    # Initialize scores
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_up_to_n = [p for p in primes if p <= n]
        if len(primes_up_to_n) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
