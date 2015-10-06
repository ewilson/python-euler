#!/usr/bin/python3


from eulermath import primes


def f(n):
    """3.29 ms to compute for 600851475143"""
    pg = primes()
    d = n
    p = next(pg)
    while d > p**2:
        if d % p == 0:
            d = d // p
        else:
            p = next(pg)
    return d


def f_test():
    assert 6857 == f(600851475143)


if __name__ == '__main__':
    print(f(600851475143))
