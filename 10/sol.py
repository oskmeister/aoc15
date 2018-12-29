s = '1321131112'

def go(s):
    res = ''
    prev = 'z'
    cnt = 1
    for i in xrange(len(s)):
        if prev == s[i]:
            cnt += 1
        else:
            if prev != 'z':
                res += (str(cnt))
                res += (prev)
            cnt = 1
        prev = s[i]
    if prev != 'z':
        res += (str(cnt))
        res += (prev)
    return res

for i in xrange(50):
    s = go(s)
print len(s)
