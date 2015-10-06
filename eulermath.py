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
    """Returns all primes less than n"""
    found_primes = [2]
    a = 3
    while a < n:
        for p in found_primes:
            if p**2 > a:
                found_primes.append(a)
                a += 2
                break
            elif a % p == 0:
                a += 2
                break
    return found_primes


def test_primes():
    pg = primes()
    p_list = []
    for _ in range(10):
        p_list.append(next(pg))

    assert [2, 3, 5 ,7, 11, 13, 17, 19, 23, 29] == p_list


def test_primes_less():
    assert [2, 3, 5 ,7, 11, 13, 17, 19] == primes_less(20)
