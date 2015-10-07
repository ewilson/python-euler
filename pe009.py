def f(n):
    """Hundreds of ms -- and O(n^2). Some number theory would help"""
    t = triples(n)[0]
    return t[0]*t[1]*t[2]


def triples(n):
    return [(a, b, n - a - b) for a in range(n // 3) for b in range(a, n // 2) if a**2 + b**2 == (n - a - b)**2]


def test_f():
    assert 31875000 == f(1000)
