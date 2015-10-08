def primes():
    """Returns a generator that produces primes lazily"""
    yield 2
    found_primes = [2]
    a = 3
    while True:
        for p in found_primes:
            if p**2 > a:
                found_primes.append(a)
                yield a
                a += 2
                break
            elif a % p == 0:
                a += 2
                break


def primes_less(n):
    """under 2 seconds for 2 million"""
    from math import sqrt, floor
    test_nums = list(range(3, floor(sqrt(n)), 2))
    prime_flags = [True] * ((n - 2) // 2)
    for a in test_nums:
        next_div = a**2
        while next_div < n:
            prime_flags[(next_div-3)//2] = False
            next_div += 2*a
    return [2] + [2*i + 3 for i, flag in enumerate(prime_flags) if flag]


def test_primes():
    pg = primes()
    p_list = []
    for _ in range(10):
        p_list.append(next(pg))

    assert [2, 3, 5 ,7, 11, 13, 17, 19, 23, 29] == p_list


def test_primes_less():
    assert [2, 3, 5, 7, 11, 13, 17, 19] == primes_less(20)
