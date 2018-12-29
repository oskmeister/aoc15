import sys
import re

lines = sys.stdin.readlines()
for line in lines:
    line = line.strip()
    op = 2
    if ' off ' in line:
        op = 0
    if ' on ' in line:
        op = 1
    x1, x2, y1, y2 = map(int, re.findall(r'-?\d+', line))
    print op, x1, x2, y1, y2
