import sys

t = []
for l in sys.stdin.readlines():
    a,b,c,d,e = map(int,l.strip().split())
    t.append((a,b,c,d,e))
print t

best = 0
for i1 in xrange(101):
    rem = 100-i1
    for i2 in xrange(rem + 1):
        rem2 = 100-i1-i2
        for i3 in xrange(rem2 + 1):
            i4 = 100-i1-i2-i3
            vals = [0] * 4
            for i in xrange(4):
                vals[i] = i1 * t[0][i] + i2 * t[1][i] + i3 * t[2][i] + i4 * t[3][i]
                vals[i] = max(vals[i], 0)
            thisval = reduce(lambda x, y: x * y, vals)
            best = max(best, thisval)
print best
