import sys
deer = []
for l in sys.stdin.readlines():
    l = l.strip().split()
    name, speed, time, sleeptime = l
    speed = int(speed)
    time = int(time)
    sleeptime = int(sleeptime)
    deer.append((name,0,speed,time,sleeptime))

pos = [0]*len(deer)
score = [0]*len(deer)

for i in xrange(2503):
    for idx, d in enumerate(deer):
        running = ((i % (d[3] + d[4])) < d[3])
        if running: pos[idx] += d[2]
    bestval = 0
    best = []
    for idx, d in enumerate(deer):
        if pos[idx] > bestval:
            bestval = pos[idx]
            best = [idx]
        elif pos[idx] == bestval:
            best.append(idx)
    for idx in best:
        score[idx] += 1

print score

