import string

def f():
    triangles = [n*(n+1)/2 for n in range(25)]
    words_with_quotes = open('words042.txt').read().split(',')
    words = [w[1:-1] for w in words_with_quotes]
    letter_sums = [letter_sum(w) for w in words]
    return len([n for n in letter_sums if n in triangles])

def letter_sum(word):
    return sum([string.ascii_uppercase.find(letter) + 1 for letter in word])
