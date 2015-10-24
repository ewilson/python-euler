def f():
    """Takes about a second, much improvement possible"""
    candidates = [(a, b, a*b) for a in range(2,100) for b in range(a+1, 5000) if len(str(a) + str(b) + str(a*b)) == 9]
    actual = [t for t in candidates if pan(t)]
    return sum(set([t[2] for t in actual]))

def pan(triple):
    a,b,c = triple
    s = str(a) + str(b) + str(c)
    chars = [c for c in s]
    sset = set(chars)
    if len(sset) == 9 and '0' not in sset:
        return True
    return False


def test_f():
    45228 == f()
