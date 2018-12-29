lb = 29000000

def get_number(num):
    ans = 0
    for n in xrange(1, num+1):
        if num % n == 0:
            ans += n * 10
    return ans

at = 0
while True:
    print at
    if get_number(at) >= lb:
        print at
        break
    at += 1

