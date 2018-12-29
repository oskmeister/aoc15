import sys

d = []
s = set()

for l in sys.stdin.readlines():
    l = l.strip()
    words = l.split()
    if "=>" in l:
        d.append((words[0].strip(), words[2].strip()))
    else:
        print l
        for t in d:
            idx = -1
            k = t[0]
            v = t[1]
            print "now at ", k
            while True:
                idx = l.find(k, idx + 1)
                if idx == -1: break
                print "at ", idx
                news = l[:idx] + v + l[idx+len(k):]
                print news
                s.add(news)
print len(s)
