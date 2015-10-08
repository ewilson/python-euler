def f(n):
    k = 1
    even_half = (k + 1) // 2
    while True:
        odd_facts = len(factors(k))
        even_facts = len(factors(even_half))
        num_facts = odd_facts * even_facts
        if num_facts > n:
            return k * even_half
        k += 2
        odd_facts = len(factors(k))
        num_facts = odd_facts * even_facts
        if num_facts > n:
            return k * even_half
        even_half += 1


def test_f():
    assert 70600674 == f()


def factors(n):
    return [d for d in range(1, (n // 2) + 1) if n % d == 0] + [n]