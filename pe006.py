def f(n):
    """single digit microseconds, O(n)"""
    return sum_squared(n) - squares_summed(n)


def sum_squared(n):
    return ((n*(n+1))//2)**2


def squares_summed(n):
    return (n * (n+1) * (2*n + 1)) // 6


def test_f():
    assert 25164150 == f(100)

