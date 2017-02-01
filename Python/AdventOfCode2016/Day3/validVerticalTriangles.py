tempList1 = []
tempList2 = []
tempList3 = []
numValidTriangles = 0
lineIndex = 1
wordIndex = 0

with open('possibleTriangles.txt') as txtfile:
    for line in txtfile:
        words = line.split()

        wordIndex = 0
        for word in words:
            number = int(word)
            if wordIndex == 0:
                tempList1.append(number)
            if wordIndex == 1:
                tempList2.append(number)
            if wordIndex == 2:
                tempList3.append(number)
            
            wordIndex += 1
            
        if lineIndex % 3 == 0:
            tempList1.sort()
            tempList2.sort()
            tempList3.sort()

            if(tempList1[0] + tempList1[1] > tempList1[2]):
                numValidTriangles += 1
            if(tempList2[0] + tempList2[1] > tempList2[2]):
                numValidTriangles += 1
            if(tempList3[0] + tempList3[1] > tempList3[2]):
                numValidTriangles += 1

            del tempList1[:]
            del tempList2[:]
            del tempList3[:]

        lineIndex += 1

    print(numValidTriangles)