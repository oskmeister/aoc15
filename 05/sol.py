import sys

def is_vowel(c):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        return True
    return False

def is_nice(s):
    num_vowels = 0
    twice_in_row = False
    for idx, c in enumerate(s):
        if is_vowel(c):
            num_vowels += 1
        if idx < len(s)-1 and s[idx] == s[idx+1]:
            twice_in_row = True
    if ('ab' in s) or ('cd' in s) or ('pq' in s) or ('xy' in s):
        return False
    return twice_in_row and num_vowels >= 3

lines = sys.stdin.readlines()
ans = 0
for line in lines:
    if is_nice(line.strip()):
        ans += 1
print ans
