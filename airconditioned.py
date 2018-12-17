minions = int(input(""))

test = False

temps = []
if not test:
    for i in range(minions):
        first, second = map(int, input().split(" "))
        temps.append([])
        temps[i].append(first)
        temps[i].append(second)

for i in range(len(temps)):
    temps[i] = sorted(temps[i])

def first(temp):
    return temp[0] + temp[1]

temps.sort(key=first)
#print(temps)
deletions = 0
for i in range(len(temps)):
    #print(temps[i - deletions])
    try:
        #print("Comparing {} with {}".format(temps[i - deletions][1], temps[i - deletions + 1][0]))
        if temps[i - deletions][1] >= temps[i - deletions + 1][0]:
            temps[i - deletions + 1][1] = temps[i - deletions][1]
            #print("Removed {}".format(temps[i - deletions]))
            temps.remove(temps[i - deletions])
            deletions += 1
            #print(temps)
    except IndexError:
        pass

    try:
        if temps[i - deletions][1] == temps[i - deletions + 1][0]:
            temps.remove(item)
    except:
        pass

print(len(temps))

#[2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3]
#[2, 5], [3, 6], [4, 7], [5, 8]
#[4, 2], [2, 1], [6, 5],
#[2, 3], [3, 7], [4, 5], [5, 6]
#[2, 2], [2, 3], [3, 3], [4, 4]
#[3, 6], [3, 3], [4, 5]
