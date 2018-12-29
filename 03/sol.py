import sys
d = dict()
line = sys.stdin.readline().strip()
r = 0
c = 0
r2 = 0
c2 = 0
d[(r,c)] = 1
for num, char in enumerate(line):
    if num % 2 == 0:
        if char == '>':
            c = c + 1
        if char == '<':
            c = c - 1
        if char == '^':
            r = r - 1
        if char == 'v':
            r = r + 1
        d[(r,c)] = 1
    else:
        if char == '>':
            c2 = c2 + 1
        if char == '<':
            c2 = c2 - 1
        if char == '^':
            r2 = r2 - 1
        if char == 'v':
            r2 = r2 + 1
        d[(r2,c2)] = 1
print len(d)
