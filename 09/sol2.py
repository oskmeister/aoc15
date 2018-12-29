import sys
import itertools
from collections import defaultdict

lines = sys.stdin.readlines()
dis = defaultdict(dict)
towns = set()

for l in lines:
    l = l.strip()
    a, _, b, _, d = l.split()
    towns.add(a)
    towns.add(b)
    d = int(d)
    dis[a][b] = d
    dis[b][a] = d

best = 0
for perm in list(itertools.permutations(list(towns))):
    val = 0
    ok = True
    for idx, town in enumerate(perm):
        if idx < len(perm)-1:
            a = town
            b = perm[idx+1]
            if b in dis[a]:
                val = val + dis[a][b]
            else:
                ok = False
    if ok:
        best = max(best, val)
print best
