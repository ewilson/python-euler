def f(n):
    """10s of microseconds"""
    return sum([int(d) for d in str(2**n)])


def test_f():
    assert 1366 == f(1000)