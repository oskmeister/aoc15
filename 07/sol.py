import sys

lines = sys.stdin.readlines()
ops = []
for l in lines:
    l = l.strip()
    words = l.split(' ')
    if len(words) == 3:
        ops.append(('ASSIGN', [words[0]], words[2]))
    elif words[0] == 'NOT':
        ops.append((words[0],[words[1]], words[3]))
    else:
        ops.append((words[1],[words[0],words[2]], words[4]))

vals = dict()
found = False
vals['b'] = 16076
while not found:
    for op in ops:
        optype = op[0]
        params = op[1]
        r = op[2]
        pp = []
        for p in params:
            if p.isdigit():
                pp.append(int(p))
            elif p in vals:
                pp.append(vals[p])
        if r == 'b': continue
        if len(pp) == len(params):
            if optype == 'ASSIGN':
                vals[r] = pp[0]
            elif optype == 'NOT':
                vals[r] = ~pp[0]
            elif optype == 'AND':
                vals[r] = pp[0] & pp[1]
            elif optype == 'OR':
                vals[r] = pp[0] | pp[1]
            elif optype == 'LSHIFT':
                vals[r] = pp[0] << pp[1]
            elif optype == 'RSHIFT':
                vals[r] = pp[0] >> pp[1]
        if 'a' in vals:
            print vals['a']
            found = True
            break
