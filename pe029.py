def f(n):
    """10s of ms for 100"""
    return len(set([a**b for a in range(2, n+1) for b in range(2, n+1)]))


def test_f():
    assert 9183 == f(100)
