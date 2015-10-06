from eulermath import primes_less


def f(n):
    """19.9 microseconds to compute for 20"""
    prod = 1
    prime_divs = primes_less(n)
    for a in range(2, n + 1):
        if prod % a == 0:
            continue
        else:
            prod *= least_prime_div(a, prime_divs)
    return prod


def least_prime_div(n, prime_divs):
    if n in prime_divs:
        return n
    for p in prime_divs:
        if n % p == 0:
            return p


def test_f():
    assert 232792560 == f(20)

