CurrentPieces = input().split()
CurrentPieces = map(int, (CurrentPieces))
CorrectPieces = (1, 1, 2, 2, 2, 8)
def Differense(CPN, RPN):
    return (RPN - CPN)

for i in map(Differense, CurrentPieces, CorrectPieces):
    print(i, end = " ")
