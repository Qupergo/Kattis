L = int(input())
D = int(input())
X = int(input())

def sumOf(x):
    return sum(list((map(int, x))))


for i in range(L, D + 1):
    if sumOf(str(i)) == X:
        print(i)
        first = i
        break

Found = False
for i in range(D, L, -1):
    if sumOf(str(i)) == X:
        print(i)
        Found = True
        break

if Found == False:
    print(first)
