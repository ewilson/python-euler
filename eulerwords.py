def is_palin(n):
    ns = str(n)
    return ns == ns[::-1]


def is_bin_palin(n):
    bns = "{0:b}".format(n)
    return bns == bns[::-1]
