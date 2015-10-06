def f0(n):
    """100s of microseconds, O(n)"""
    return sum([k for k in range(n) if k % 3 == 0 or k % 5 == 0])


def f1(n):
    """10s of microseconds, O(n)"""
    return sum(range(0, n, 3)) + sum(range(0, n, 5)) - sum(range(0, n, 15))


def f2(n):
    """This is really fast, O(1)"""
    return sum_div_by(n - 1, 3) + sum_div_by(n - 1, 5) - sum_div_by(n - 1, 15)


def sum_div_by(n, d):
    p = n // d
    return d*(p*(p+1))//2


def test_f0():
    assert 23 == f0(10)


def test_f1():
    assert 23 == f1(10)


def test_f2():
    assert 233168 == f2(1000)
