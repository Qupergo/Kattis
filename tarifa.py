index = 0
mgb = input()
months = input()

whatsLeft = int(mgb)
for i in range(int(months)):
    usedThisMonth = int(input())
    whatsLeft -= usedThisMonth
    whatsLeft += int(mgb)

print(whatsLeft)
