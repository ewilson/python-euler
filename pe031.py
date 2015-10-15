coins = [200, 100, 50, 20, 10, 5, 2, 1]


def f0(vals_desc, target):
    """tens of ms for 200 pound, O(exp^n)?"""
    if len(vals_desc) == 1 and target % vals_desc[0] == 0:
        return 1
    elif len(vals_desc) > 1:
        first, rest = vals_desc[0], vals_desc[1:]
        combinations = 0
        product = 0
        while product <= target:
            combinations += f0(rest, target - product)
            product += first
        return combinations


def test_f0():
    assert 73682 == f0(coins, 200)