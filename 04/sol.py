import md5

inp = 'yzbqklnj'

at = 1
while True:
    m = md5.new()
    m.update(inp + str(at))
    s = m.hexdigest()
    if s[:6] == '000000':
        print s
        print at
        break
    at += 1
