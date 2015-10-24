from functools import lru_cache


def f(n):
    """About a 10 seconds -- good candidate for improvement"""
    longest = 1
    longest_start = 1
    for num in range(1, n):
        cl = collatz_len(num)
        if cl > longest:
            longest_start = num
            longest = cl
    return longest_start


@lru_cache(maxsize=None)
def collatz_len(n):
    if n == 1:
        return 1
    else:
        return 1 + collatz_len(collatz_step(n))


def collatz_step(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def test_f():
    assert 837799 == f(1000000)
