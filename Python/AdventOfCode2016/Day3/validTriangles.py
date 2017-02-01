tempList = []
numValidTriangles = 0

with open('possibleTriangles.txt') as txtfile:
    for line in txtfile:
        del tempList[:]
        words = line.split()

        for word in words:
            number = int(word)
            tempList.append(number)

        tempList.sort()
        if(tempList[0] + tempList[1] > tempList[2]):
            numValidTriangles += 1

    print(numValidTriangles)