import sys

d = dict()
d['children'] = 3
d['cats'] = 7
d['samoyeds'] = 2
d['pomeranians'] = 3
d['akitas'] = 0
d['vizslas'] = 0
d['goldfish'] = 5
d['trees'] = 3
d['cars'] = 2
d['perfumes'] = 1

for idx, l in enumerate(sys.stdin.readlines()):
    l = l.strip().split(',')
    l[0] = "".join(l[0].split(' ')[2:])

    ok = True
    for v in l:
        k, v = v.split(':')
        k = k.strip()
        v = int(v.strip())
        if k in d and d[k] != v:
            ok = False
    if ok:
        print idx+1
        break
