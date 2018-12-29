import sys
import re

lines = sys.stdin.readlines()
s = 0
for l in lines:
    s = s + sum(map(int, re.findall(r'-?\d+', l)))
print s
