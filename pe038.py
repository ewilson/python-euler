def f():
    n = 2
    while n < 10000:
        r = make_pan(n)
        if r:
            print(r)
        n += 1


def make_pan(k):
    s = ''
    i = 1
    while len(s) < 9:
        s += str(i*k)
        i += 1
    if sorted(s) == [str(j) for j in range(1,10)]:
        return k, s
    else:
        return False
