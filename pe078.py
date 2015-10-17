from functools import lru_cache


def f(n):
    return p(n, n)


def f2(n):
    """Errors, and takes 4s for 1000"""
    part_list = n * [1]
    count = 1
    while part_list[0] < n:
        print(part_list)
        part_list = next_part(n, part_list)
        count += 1
    return count


def next_part(n, li):
    highest = li[0]
    lowest = li[-1]
    first_lowest = li.index(lowest)
    current_start = li[:first_lowest]
    if sum(current_start) + lowest + 1 > n or highest == lowest:
        return fill(n, highest + 1)
    elif sum(current_start) + lowest + 1 == n:
        return current_start + [lowest + 1]
    else:
        print('nb')
        return current_start + [lowest + 1] + fill(n - sum(current_start) - (lowest + 1), lowest)


def fill(target, highest):
    if highest == 1:
        return [1] * target
    else:
        return [highest] + [1] * (target - highest)


@lru_cache(maxsize=None)
def p(highest, target):
    """From 31 -- works up to 328"""
    if highest == 1 or highest == 0:
        return 1
    elif highest > target:
        return p(target, target)
    else:
        combinations = 0
        product = 0
        while product <= target:
            combinations += p(highest - 1, target - product)
            product += highest
        return combinations


@lru_cache(maxsize=None)
def p2(target, highest, lowest):
    print(target, highest, lowest)
    """From 31 -- works up to 328"""
    if highest == lowest:
        return 1 if target % highest == 0 else 0
    elif highest > target:
        return p2(target, target, lowest)
    else:
        combinations = 0
        product = 0
        while product <= target:
            combinations += p2(target - product, highest - 1, lowest + 1)
            product += highest
        return combinations


def test_f0():
    pass