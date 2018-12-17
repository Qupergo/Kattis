h, m = map(int, input().split())

m -= 45
if m < 0:
    m += 60
    if h != 00:
        h -= 1
    elif h == 00:
        h = 23

print(str(h) + " " + str(m))
