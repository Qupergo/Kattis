#1984 2 -> #9184 1 -> 9814
#210 1 -> 201
#666 3 -> 666
#9090 2 -> 9900 1 -> 9900
#9281281 5 -> 9882211
#993 3 -> 993


#Take Input
twoSimiliarNumbersBesideEachother = False
Number, Swaps = input().split()
swapped = [0]
#Divide numbers up individually
NumbersToSwap = list(Number)
Swaps = int(Swaps)

def FindMostUnderusedValue(numList, swapped):
    #Variable to check for highest number
    currentNum = 9

    #for loop 1-9
    for i in range(1, 10):
#        print("Is {} in {}?".format(currentNum, numList))
        if str(currentNum) in numList:
            index = len(numList) - numList[::-1].index(str(currentNum)) - 1
            if index not in swapped:
#                print("The swapped numbers are {}".format(swapped))
#                print("The index is {}".format(index))
                return index
        currentNum -= 1
    return 0


#Run loop for each swap availiable
swapsLeft = Swaps
for i in range(Swaps):
#    print(swapsLeft)+-
#    print(sorted(NumbersToSwap)[::-1] == NumbersToSwap)
    if sorted(NumbersToSwap)[::-1] == NumbersToSwap:

        #If there is an even amount of swaps left

        if (swapsLeft) % 2 == 0:

            #the swap would swap once and then back so just break
#            print("Even swaps nothing was swapped")
            break

        #if there is an odd amount of swaps left
        elif swapsLeft % 2 != 0:
            #In this case it would have swapped several times but will end up with this in the end
            for i in range(len(NumbersToSwap)):
                if i + 1 < len(NumbersToSwap):
                    if NumbersToSwap[i] == NumbersToSwap[i + 1]:
                        twoSimiliarNumbersBesideEachother = True

#            print("Odd swaps swapped last two digits")
            if not twoSimiliarNumbersBesideEachother:
                NumbersToSwap[-1], NumbersToSwap[-2] = NumbersToSwap[-2], NumbersToSwap[-1]
            break

    #find the most underused value
    valueIndex = FindMostUnderusedValue(NumbersToSwap, swapped)

    #Swap it to the front if it is larger than that number otherwise check the next one in list
    for i in range(len(NumbersToSwap)):
#        print("The current list is {}".format(NumbersToSwap))
#        print("The most underused value is {} and the current swap target is {}".format(NumbersToSwap[valueIndex], NumbersToSwap[i]))
#        print("The index is {} and the swap target index is {}".format(valueIndex, i))

        if NumbersToSwap[valueIndex] == NumbersToSwap[i] and valueIndex - i == 1:
            #If two numbers are the same no need to swap
            swapped.append(valueIndex)
            break


        if NumbersToSwap[valueIndex] > NumbersToSwap[i] and valueIndex > i:
            NumbersToSwap[valueIndex], NumbersToSwap[i] = NumbersToSwap[i], NumbersToSwap[valueIndex]
            swapped.append(i)
            swapsLeft -= 1
#            print("The current list is {}".format(NumbersToSwap))
            break

        if NumbersToSwap[valueIndex] < NumbersToSwap[i] and valueIndex < i:
            NumbersToSwap[valueIndex], NumbersToSwap[i] = NumbersToSwap[i], NumbersToSwap[valueIndex]
            swapped.append(i)
            swapsLeft -= 1
            break

#    print(sorted(NumbersToSwap)[::-1] == NumbersToSwap)
    if sorted(NumbersToSwap)[::-1] == NumbersToSwap:

        #If there is an even amount of swaps left

        if (swapsLeft) % 2 == 0:
            #the swap would swap once and then back so just break
#            print("Even swaps nothing was swapped")
            break

        #if there is an odd amount of swaps left
        elif swapsLeft % 2 != 0:
            #In this case it would have swapped several times but will end up with this in the end
#            print("Odd swaps swapped last two digits")
            for i in range(len(NumbersToSwap)):
                if i + 1 > len(NumbersToSwap):
                    if NumbersToSwap[i] == NumbersToSwap[i + 1]:
                        break

            NumbersToSwap[-1], NumbersToSwap[-2] = NumbersToSwap[-2], NumbersToSwap[-1]
            break



print("".join(NumbersToSwap))
