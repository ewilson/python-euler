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

