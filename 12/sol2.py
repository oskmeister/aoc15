import json
import sys

ans = 0

def go(obj):
    if isinstance(obj, dict):
        ok = True
        for k in obj:
            if obj[k] == 'red':
                ok = False
        s = 0
        if ok:
            for k in obj:
                s = s + go(obj[k])
        return s
    elif isinstance(obj, list):
        s = 0
        for k in obj:
            s = s + go(k)
        return s
    else:
        if isinstance(obj, int):
            return obj
        return 0

l = sys.stdin.readline().strip()
o = json.loads(l)
print go(o)


