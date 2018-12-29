import sys
from heapq import *

d = []
s = set()

def neighbours(d, s):
    res = []
    for t in d:
        idx = -1
        k = t[1]
        v = t[0]
        while True:
            idx = s.find(k, idx + 1)
            if idx == -1: break
            news = s[:idx] + v + s[idx+len(k):]
            res.append(news)
    return res

def astar(source, target, d):
    dist = dict()
    dist[source] = 0
    q = [(len(source), source)]
    qidx = 0
    while q:
        _, cur = heappop(q)
        print cur
        qidx += 1
        if cur == target:
            return dist[target]
        for n in neighbours(d, cur):
            if n in dist: continue
            heappush(q, (len(n), n))
            dist[n] = dist[cur]+1
    return 0

for l in sys.stdin.readlines():
    l = l.strip()
    words = l.split()
    if "=>" in l:
        d.append((words[0].strip(), words[2].strip()))
    else:
        print astar(l, 'e', d)
