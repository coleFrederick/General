import re

isXYX = False #for given character pattern xyx outside brackets, yxy must exist inside brackets
numXYXlines = 0
allTriples = []
inBrackets = []

def findTriples(triple):
    for index in range(0, len(triple) - 3 + 1): # +1 because end of range is exclusive
        newString = triple[index] + triple[index + 1] + triple[index + 2] 
        if newString[0] == newString[-1] and newString[0] != newString[1]:
            allTriples.append(newString)
    return

def storeBracketData(string):
    inBrackets.append(string)
    return

def matchFound():
    for triple in allTriples:
        converseTriple = triple[1] + triple[0] + triple[1]
        for bracketString in inBrackets:
            testString = ""
            for char in range(0, len(bracketString) - 3 + 1):
                testString = bracketString[char] + bracketString[char + 1] + bracketString[char + 2]
                if converseTriple == testString:
                    return True
    return False

with open('realText.txt') as txtfile:
    #read in all data
    for line in txtfile:
        isXYX = False

        cleanline = line.split('\n')[0]

        firstChunk = cleanline.split('[')[0]
        findTriples(firstChunk)

        firstChunk += "["
        cleanline = cleanline.split(firstChunk, 1)[1]

        #get lists of triples to check and strings to cehck against
        while cleanline != "":
            secondChunk = cleanline.split(']')[0]
            storeBracketData(secondChunk)
            secondChunk += "]"
            remainder = cleanline.split(secondChunk, 1)[1]
            if '[' in remainder:
                firstChunk = remainder.split('[')[0]
                findTriples(firstChunk)
                firstChunk += "["
                cleanline = cleanline.split(firstChunk, 1)[1]
            else:
                firstChunk = remainder
                findTriples(firstChunk)
                cleanline = ""

        #check if any triples have their converses in any of the strings 
        if matchFound():
            numXYXlines += 1
        allTriples = []
        inBrackets = []

    print(numXYXlines)