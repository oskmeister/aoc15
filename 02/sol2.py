import sys

lines = sys.stdin.readlines()
ans = 0
for line in lines:
    l, w, h = map(int, line.strip().split('x'))
    a = sorted([l, w, h])
    ans = ans + l*w*h + a[0]*2 + a[1]*2
print ans
