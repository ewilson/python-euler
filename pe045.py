
def f():
    hg = h(143)
    pg = p(165)
    next(pg), next(hg)
    h_num, p_num = next(hg), next(pg)
    while h_num[1] != p_num[1]:
        if h_num[1] < p_num[1]:
            h_num = next(hg)
        else:
            p_num = next(pg)

    print("P: {0}, H: {1}".format(p_num, h_num))

        

def t(n):
    v = int(n*(n+1)/2)
    while True:
        yield (n, v)
        n += 1
        v += n

def h(n):
    v = n*(2*n-1)
    while True:
        yield (n, v)
        v += 4*n + 1
        n += 1

def p(n):
    v = int(n*(3*n-1)/2)
    while True:
        yield (n, v)
        v += 3*n + 1
        n += 1
