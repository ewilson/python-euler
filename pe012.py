from math import sqrt, floor


factors_cache = {}


def f(n):
    """Under 200 ms for 500

    Main optimization here is that every triangular number is of the for n*(n+1)/2. Since these two integer
    factors are relatively prime, it is easy to compute the number of factors of the product quickly.

    Also using a cache to avoid computing factor count multiple times. Making more use of that cache by
    factoring all powers of two before looking up or computing numbers of factors.

    Full prime factorization might lead to even better performance.
    """
    factors_cache.clear()
    odd_part = 1
    half_even_part = (odd_part + 1) // 2
    odd_facts = num_facts(odd_part)
    even_facts = num_facts(half_even_part)
    while True:
        triangle = odd_part * half_even_part
        if odd_part < 2 * half_even_part:
            even_facts = num_facts(half_even_part)
            odd_part += 2
        else:
            odd_facts = num_facts(odd_part)
            half_even_part += 1
        if odd_facts * even_facts > n:
            return triangle


def factors(n):
    """Stopping at square root turns out to be essential for performance

    Every factor below sqrt has a corresponding factor above"""
    root = sqrt(n)
    int_root = floor(root)
    facts = 2*len([d for d in range(1, int_root + 1) if n % d == 0])
    if root == int_root:
        # perfect square, double counted sqrt
        facts -= 1
    return facts


def num_facts(m):
    """Caching optimization"""
    if m in factors_cache:
        return factors_cache[m]
    elif m % 2 == 0:
        twos, odd = pull_twos(m)
        return (twos + 1) * factors_cache[odd]
    else:
        fact_n = factors(m)
        factors_cache[m] = fact_n
        return fact_n


def pull_twos(n):
    """n = 2^d * m, returns d and m

    This is useful since factors(n) ==  (d+1) * factors(m)
    Accomplishes a performance increase of ~30%"""
    d = 0
    while n % 2 == 0:
        n //= 2
        d += 1
    return d, n


def test_f():
    assert 76576500 == f(500)
