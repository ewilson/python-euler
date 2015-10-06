def f0(n):
    """Nearly a second for 3"""
    rng = range(10**(n - 1), 10**n)
    return max([x*y for x in rng for y in rng if is_palin(x*y)])


def f1(n):
    """Single digit ms. O(terrible)"""
    low = 10**(n - 1) - 1
    hi = 10**n - 1
    best = 0
    for x in range(hi, low, -1):
        for y in range(x, low, -1):
            prod = x*y
            if prod < best:
                # if prod < best when y is hi, we are done
                # if y is smaller, maybe a new x will work better
                if y == x:
                    return best
                else:
                    break
            if is_palin(prod):
                if prod > best:
                    best = prod


def is_palin(n):
    ns = str(n)
    return ns == ns[::-1]


def test_f0():
    assert 9009 == f0(2)


def test_f1():
    assert 906609 == f1(3)
