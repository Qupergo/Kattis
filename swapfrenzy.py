numberToSwap, timesToSwap = map(int, input().split())

swapped = [0]

def findHighestNumIndexFromList(numList, alreadySwapped):
    for i in range(9, 0, - 1):
        index = len(numList) - 1
        for j in numList[::-1]:
#            print("The current number in range is {}, The current number in numlist is {}".format(i, j))
            if int(j) == i and index not in alreadySwapped:
                    return index
            else:
                index -= 1
    return findLowestNumIndexFromList(numList)

def findLowestNumIndexFromList(numList):
    for i in range(0, 9, 1):
        index = len(numList) - 1
        for j in numList[::-1]:
#            print("The current number in range is {}, The current number in numlist is {}".format(i, j))
            if int(j) == i and numList.index(j):
#                print("These are equal")
                return index
            else:
#                print("These are not equal")
                index -= 1

numbersToSwap = list(str(numberToSwap))
swapsLeft = timesToSwap
for i in range(timesToSwap):
    highNum = findHighestNumIndexFromList(numbersToSwap, swapped)
    #print("The highest number is " + numbersToSwap[highNum])
    Swaped = False
    while not Swaped:
        try:
            for j in range(len(numbersToSwap)):
                if j > highNum:
                    if int(numbersToSwap[highNum]) < int(numbersToSwap[j]):
                        numbersToSwap[highNum], numbersToSwap[j] = numbersToSwap[j], numbersToSwap[highNum]
                        swapsLeft -= 1
                        swapped.append(j)
                        Swaped = True
                        break

                elif j < highNum:
                        if int(numbersToSwap[highNum]) > int(numbersToSwap[j]):
                            numbersToSwap[highNum], numbersToSwap[j] = numbersToSwap[j], numbersToSwap[highNum]
                            swapsLeft -= 1
                            swapped.append(j)
                            Swaped = True
                            break
#                            print("Swapped {} and {}".format(numbersToSwap[highNum], numbersToSwap[j]))
#                            print("New list is {}".format(numbersToSwap))
                else:
                    swapped.append(j)
                    highNum = findLowestNumIndexFromList(numbersToSwap)
                    continue



        except TypeError:
                    pass
#print("Swaps left: " + str(swapsLeft))
if len(numbersToSwap) == 2:
    numbersToSwap[1], numbersToSwap[0] = numbersToSwap[0], numbersToSwap[1]
if int(numbersToSwap[0]) == 0:
    numbersToSwap.remove("0")
print("".join(numbersToSwap))
