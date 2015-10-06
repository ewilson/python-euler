#!/usr/bin/python3


def f0(n):
    """404 microseconds for 100"""
    return sum([k for k in range(n) if k % 3 == 0 or k % 5 == 0])


def f1(n):
    """29 microseconds for 100"""
    return sum(range(0, n, 3)) + sum(range(0, n, 5)) - sum(range(0, n, 15))


def test_f0():
    assert 233168 == f0(1000)


def test_f1():
    assert 233168 == f1(1000)


if __name__ == '__main__':
    print(f1(1000))

