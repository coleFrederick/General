import collections

numCharsInRow = 8
charLists = ["" for x in range(numCharsInRow)]

message = ""

with open('dataSet.txt') as txtfile:
    #read in all data
    for line in txtfile:
        for index in range(0, numCharsInRow):
            charLists[index] += line[index]

    for index in range(0, numCharsInRow):
        charCount = collections.Counter(charLists[index]).most_common()
        message += charCount[0][0]
    
    print(message)