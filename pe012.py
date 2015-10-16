from math import sqrt, floor
from functools import lru_cache


def f(n):
    """Under 20 ms for 500

    Main optimization here is that every triangular number is of the for n*(n+1)/2. Since these two integer
    factors are relatively prime, it is easy to compute the number of factors of the product quickly.

    Also using a cache to avoid computing factor count multiple times.

    Full prime factorization might lead to even better performance.
    """
    odd_part = 1
    half_even_part = (odd_part + 1) // 2
    odd_facts = factors(odd_part)
    even_facts = factors(half_even_part)
    while True:
        triangle = odd_part * half_even_part
        if odd_part < 2 * half_even_part:
            even_facts = factors(half_even_part)
            odd_part += 2
        else:
            odd_facts = factors(odd_part)
            half_even_part += 1
        if odd_facts * even_facts > n:
            return triangle


@lru_cache(maxsize=None)
def factors(n):
    """Stopping at square root turns out to be essential for performance

    Every factor below sqrt has a corresponding factor above"""
    root = sqrt(n)
    int_root = floor(root)
    facts = 2*len([d for d in range(1, int_root + 1) if n % d == 0])
    if root == int_root:
        # perfect square, double counted sqrt
        facts -= 1
    return facts


def test_f():
    assert 76576500 == f(500)
