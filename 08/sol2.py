import sys
import re
lines = sys.stdin.readlines()
a = 0
for l in lines:
    l=l.strip()
    a = a+2+len(re.escape(l))-len(l)
print a
