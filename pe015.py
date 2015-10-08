from math import factorial


def f(n):
    """few microseconds, with no optimization of binom"""
    return binom(2*n, n)


def binom(m, n):
    return factorial(m) // (factorial(n) * factorial(m-n))


def test_f():
    assert 137846528820 == f(20)
