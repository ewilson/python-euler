from operator import mul
from functools import reduce


def f(ns):
    return reduce(mul, d(ns), 1)

def d(ns):
    digit = 0
    num = 0
    results = []
    for n in ns:
        while digit < n:
            num += 1
            digit += len(str(num))
        results.append(int(str(num)[n-digit-1]))
    return results

def test_d():
    nums = [1, 10, 100, 1000]
    
    assert d(nums) == [1, 1, 5, 3]

def test_f():
    nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 1000000]

    assert f(nums) == 210
