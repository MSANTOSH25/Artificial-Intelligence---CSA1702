from itertools import permutations

word1 = "SEND"
word2 = "MORE"
result = "MONEY"

letters = "SENDMORY"

for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))

    if d["S"] == 0 or d["M"] == 0:
        continue

    n1 = int("".join(str(d[c]) for c in word1))
    n2 = int("".join(str(d[c]) for c in word2))
    n3 = int("".join(str(d[c]) for c in result))

    if n1 + n2 == n3:
        print("Solution found:")
        print("SEND =", n1)
        print("MORE =", n2)
        print("MONEY =", n3)
        break
