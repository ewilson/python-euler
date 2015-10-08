from eulermath import primes


def f(n):
    """sindle-digit ms to compute for 600851475143"""
    pg = primes()
    d = n
    p = next(pg)
    while d > p**2:
        if d % p == 0:
            d = d // p
        else:
            p = next(pg)
    return d


def test_f():
    assert 6857 == f(600851475143)
