from itertools import permutations

perm = permutations([1, 2, 3, 4], 2)

for p in perm:
    print(sum(p))
