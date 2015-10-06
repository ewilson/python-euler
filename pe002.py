#!/usr/bin/python3


def f(n):
    """13.3 microseconds for 4000000"""
    a, b = 1, 1
    s = 0
    while a < n:
        a, b = a+b, a
        if a % 2 == 0:
            s += a
    return s


def test_f():
    assert 4613732 == f(4000000)


if __name__ == '__main__':
    print(f(4000000))
