from eulermath import primes_less


def f(n):
    """Several seconds :("""
    return sum(primes_less(n))


def test_f():
    assert 142913828922 == f(2000000)
