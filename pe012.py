from math import sqrt, floor


def f(n):
    """Under 200 ms for 500"""
    k = 1
    even_half = (k + 1) // 2
    factors_cache = {}

    def num_facts(m):
        if m in factors_cache:
            return factors_cache[m]
        elif m % 2 == 0:
            twos, odd = pull_twos(m)
            return twos * factors_cache[odd]
        else:
            fact_n = factors(m)
            factors_cache[m] = fact_n
            return fact_n

    while True:
        odd_facts = num_facts(k)
        even_facts = num_facts(even_half)
        facts = odd_facts * even_facts
        if facts > n:
            return k * even_half
        k += 2
        odd_facts = num_facts(k)
        facts = odd_facts * even_facts
        if facts > n:
            return k * even_half
        even_half += 1


def factors(n):
    root = floor(sqrt(n))
    return 2*len([d for d in range(1, root) if n % d == 0])


def pull_twos(n):
    d = 1
    while n % 2 == 0:
        n //= 2
        d += 1
    return d, n


def test_f():
    assert 76576500 == f(500)
