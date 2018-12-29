import sys

def is_nice(s):
    found = False
    found2 = False
    for idx, c in enumerate(s):
        if idx < len(s)-1:
            s2 = s[0:idx]
            s3 = s[idx+2:len(s)]
            if s[idx:idx+2] in s2 or s[idx:idx+2] in s3:
                found2 = True
        if idx < len(s)-2:
            if s[idx] == s[idx+2]:
                found = True
    return found and found2

lines = sys.stdin.readlines()
ans = 0
for line in lines:
    if is_nice(line.strip()):
        ans += 1
print ans
