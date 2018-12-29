import sys
import copy
grid = []
for l in sys.stdin.readlines():
    grid.append(list(l.strip()))

size = len(grid)

for i in xrange(100):
    grid[0][0] = '#'
    grid[99][0] = '#'
    grid[0][99] = '#'
    grid[99][99] = '#'
    ng = copy.deepcopy(grid)
    for r in xrange(size):
        for c in xrange(size):
            n_on = 0
            for dr in xrange(-1, 2):
                for dc in xrange(-1, 2):
                    if dr == 0 and dc == 0: continue
                    nr = r + dr
                    nc = c + dc
                    if nr >= 0 and nr < size and nc >= 0 and nc < size:
                        if grid[nr][nc] == '#':
                            n_on += 1
            if grid[r][c] == '.':
                if n_on == 3:
                    ng[r][c] = '#'
                else:
                    ng[r][c] = '.'
            else:
                if n_on == 3 or n_on == 2:
                    ng[r][c] = '#'
                else:
                    ng[r][c] = '.'
    ng[0][0] = '#'
    ng[99][0] = '#'
    ng[0][99] = '#'
    ng[99][99] = '#'
    grid = copy.deepcopy(ng)

ans = 0
for i in xrange(size):
    for j in xrange(size):
        if grid[i][j] == '#':
            ans += 1
print ans
