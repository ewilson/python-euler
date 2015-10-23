from eulermath import primes_less, is_prime


def find_pairs(N):
    ps = primes_less(N+1)
    return [(a, b) for b in ps for a in range(-b, N+1)]


def find_best_pair(N):
    """Works but far too slow --- ~10 s"""
    pairs = find_pairs(N)
    best_pair, longest = None, 0
    for pair in pairs:
        length = max_prime_list(pair)
        if length > longest:
            longest = length
            best_pair = pair
    return best_pair, longest


def max_prime_list(pair):
    a, b = pair
    prime_seq_len = 0
    n = 0
    while n < b:
        q = n**2 + a*n + b
        if q > 1 and is_prime(q):
            prime_seq_len += 1
            n += 1
        else:
            break
    return prime_seq_len