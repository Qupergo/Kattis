wordAmount = input()

words = []
for i in range(int(wordAmount)):
    words.append(input())

Turn = 1
fairGame = True
triedWords = []
for i in range(len(words)):

    if words[i] in triedWords:
        fairGame = False
        break

    if i + 1 < len(words):
        if words[i][-1] == words[i + 1][0]:
            triedWords.append(words[i])

        else:
            fairGame = False
            Turn += 1
            break

    Turn += 1

if fairGame:
    print("Fair Game")

elif Turn % 2 == 0:
    print("Player 2 lost")
else:
    print("Player 1 lost")
