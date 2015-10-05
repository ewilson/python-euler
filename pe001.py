#!/usr/bin/python3


def f0(n):
    """Pythonic solution -- easy to read by slow"""
    return sum([k for k in range(n) if k % 3 == 0 or k % 5 == 0])


def f1(n):
    """No divisibility checks, ~15x faster"""
    return sum(range(0, n, 3)) + sum(range(0, n, 5)) - sum(range(0, n, 15))


if __name__ == '__main__':
    print(f1(1000))
