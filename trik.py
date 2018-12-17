Movement = input()
CurrentPosition = 1

def MoveA(cp):
    if cp == 1:
        cp += 1
    elif cp == 2:
        cp -= 1
    elif cp == 3:
        cp = cp
    return cp

def MoveB(cp):
    if cp == 1:
        cp = cp
    elif cp == 2:
        cp += 1
    elif cp == 3:
        cp -= 1
    return cp

def MoveC(cp):
    if cp == 1:
        cp += 2
    elif cp == 2:
        cp = cp
    elif cp == 3:
        cp -= 2
    return cp

for i in Movement:
    if i == "A":
        CurrentPosition = MoveA(CurrentPosition)
    if i == "B":
        CurrentPosition = MoveB(CurrentPosition)
    if i == "C":
        CurrentPosition = MoveC(CurrentPosition)
print(CurrentPosition)
