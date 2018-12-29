import sys
from collections import defaultdict
from itertools import cycle, permutations

names = set()
d = defaultdict(dict)

for l in sys.stdin.readlines():
    l = l.strip().split()
    a = l[0]
    b = l[-1][:-1]
    diff = int(l[3])
    if l[2] == 'lose':
        diff = -diff
    d[a][b] = diff
    names.add(a)
    names.add(b)

best = -1000000000
for perm in permutations(list(names)):
    score = 0
    for i, n in enumerate(perm):
        pn = perm[i-1] if i > 0 else perm[len(perm)-1]
        nn = perm[i+1] if i < len(perm)-1 else perm[0]
        if pn in d[n]:
            score = score + d[n][pn]
        if nn in d[n]:
            score = score + d[n][nn]
    best = max(score, best)
print best


