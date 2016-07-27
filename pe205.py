from collections import Counter
from math import factorial


def f():
    p_counts = count(9, 4)
    c_counts = count(6, 6)
    wlt = Counter()
    for p_val in p_counts:
        for c_val in c_counts:
            times = p_counts[p_val] * c_counts[c_val]
            if p_val > c_val:
                wlt.update({'W': times})
            elif p_val < c_val:
                wlt.update({'L': times})
            else:
                wlt.update({'T': times})
    return wlt['W'] / sum(wlt.values())


def count(n, m):
    c = Counter()
    for roll in possible_rolls(n, m):
        r = Result(roll)
        c.update({r.sum(): int(r.count())})
    return c


def possible_rolls(n, m):
    if n == 1:
        return [[i] for i in range(1, m+1)]
    else:
        stuff = []
        new = list(range(1, m+1))
        old = possible_rolls(n-1, m)
        for n in new:
            for group in old:
                if n <= min(group):
                    entry = [n]
                    entry.extend(group)
                    stuff.append(entry)
        return stuff

class Result():
    def __init__(self, rolls):
        self.num = len(rolls)
        self.rolls = Counter(rolls)

    def count(self):
        denom = 1
        for n in self.rolls:
            denom *= factorial(self.rolls[n])
        return factorial(self.num)/denom

    def sum(self):
        return sum(self.rolls.elements())
