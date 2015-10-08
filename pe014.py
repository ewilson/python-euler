cl_cache = {}


def f(n):
    """About 4 seconds -- which is much, much better than without the cache"""
    cl_cache.clear()
    longest = 1
    longest_start = 1
    for num in range(1, n):
        cl = collatz_len(num)
        if cl > longest:
            longest_start = num
            longest = cl
    return longest_start


def collatz_len(n):
    if n == 1:
        return 1
    elif n in cl_cache:
        return cl_cache[n]
    else:
        cl = 1 + collatz_len(collatz_step(n))
        cl_cache[n] = cl
        return cl


def collatz_step(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def test_f():
    assert 837799 == f(1000000)
