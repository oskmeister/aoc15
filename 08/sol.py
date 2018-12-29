import sys
lines = sys.stdin.readlines()
a = 0
for l in lines:
    l=l.strip()
    a = a+len(l)-len(eval(l))
print a
