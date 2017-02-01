import re

isABBA = [False, False]
numABBAlines = 0

def isAbba( string, arrayIndex):
    for index in range(0, len(string) - 4 + 1): # +1 because end of range is exclusive
        newString = ""
        for char in range(index, index + 4):
            newString += string[char]
    
        if newString[0] == newString[-1] and newString[1] == newString[-2] and newString[0] != newString[1]:
            isABBA[arrayIndex] = True
    return

with open('realText.txt') as txtfile:
    #read in all data
    for line in txtfile:
        isABBA = [False, False]

        cleanline = line.split('\n')[0]

        firstChunk = cleanline.split('[')[0]
        isAbba(firstChunk, 0)
        firstChunk += "["
        cleanline = cleanline.split(firstChunk, 1)[1]

        while cleanline != "":
            secondChunk = cleanline.split(']')[0]
            secondChunk += "]"
            remainder = cleanline.split(secondChunk, 1)[1]
            if '[' in remainder:
                firstChunk = remainder.split('[')[0]
                firstChunk += "["
                cleanline = cleanline.split(firstChunk, 1)[1]
            else:
                firstChunk = remainder
                cleanline = ""

            isAbba(secondChunk, 1)

            if isABBA[1] == True:
                cleanline = ""
                continue
            elif isABBA[0] == True:
                continue
            else:
                isAbba(firstChunk, 0)

        if isABBA[0] == True and isABBA[1] == False:
            numABBAlines += 1

    print(numABBAlines)