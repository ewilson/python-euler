def f():
    triples = [(a,b,c) for a in range(1,10) for b in range(1,10) for c in range(1,10) if 9*a*c + c*b == 10*a*b and 10*a+b < 10*b+c]
    print(triples)
    n, d = 1,1
    for t in triples:
        n *= t[0]
        d *= t[2]
    return (n, d)
