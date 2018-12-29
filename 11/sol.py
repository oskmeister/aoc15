pw = list('hepxxzaa')

def is_valid(s):
    inc = False
    diffp = False
    for i, c in enumerate(s):
        if i < len(s)-2:
            if ord(s[i])+1 == ord(s[i+1]) and ord(s[i+1])+1 == ord(s[i+2]):
                inc = True
        if i < len(s)-1:
            if s[i] == s[i+1]:
                for j in xrange(len(s)-1):
                    if i >= j-1 and j < i+2:
                        continue
                    if s[j] == s[j+1]:
                        diffp = True
    if 'i' in s or 'o' in s or 'l' in s:
        return False
    return inc and diffp

def incr(s):
    at = len(s)-1
    while at >= 0:
        if s[at] < 'z':
            s[at] = chr(ord(s[at]) + 1)
            break
        at -= 1
    at += 1
    while at < len(s):
        s[at] = 'a'
        at += 1
    return s

while True:
    if is_valid(pw):
        print "".join(pw)
        break
    pw = incr(pw)
