from eulermath import is_prime


def f():
    """hundreds of ms"""
    return sum(build_list())


def build_list():
    left = [2, 3, 5, 7]
    right = [3, 7]
    tp = []
    while len(tp) < 11:
        tp.extend(extend(left, right))
        left = extend_left(left)
        right = extend_right(right)
    return tp


def extend(left, right):
    candidates = [a*10 + b%10 for a in left for b in right if str(a)[1:] == str(b)[:-1]]
    return [p for p in candidates if is_prime(p)]


def extend_left(left):
    candidates = [a*10 + b for a in left for b in [1, 3, 7, 9]]
    return [p for p in candidates if is_prime(p)]


def extend_right(right):
    candidates = [int(str(n) + str(p)) for p in right for n in range(1,10)]
    return [p for p in candidates if is_prime(p)]


def test_f():
    assert 748317 == f()
