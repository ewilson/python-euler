#!/usr/bin/python3


def f(n):
    a, b = 1, 1
    s = 0
    while a < n:
        a, b = a+b, a
        if a % 2 == 0:
            s += a
    return s


if __name__ == '__main__':
    print(f(4000000))
