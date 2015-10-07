from eulerwords import is_palin, is_bin_palin


def f(n):
    return sum([a for a in range(n) if is_palin(a) and is_bin_palin(a)])


def test_f():
    assert 872187 == f(1000000)
