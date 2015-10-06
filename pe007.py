import itertools

from eulermath import primes


def f(n):
    """hundreds of ms. Good enough for now."""
    pg = primes()
    p = itertools.islice(pg, n-1, n)
    return next(p)


def test_f():
    assert 104743 == f(10001)
