import sys

lines = sys.stdin.readlines()
ans = 0
for line in lines:
    l, w, h = map(int, line.strip().split('x'))
    a = sorted([l, w, h])
    ans = ans + 2*l*w + 2*w*h + 2*h*l + a[0]*a[1]
print ans
