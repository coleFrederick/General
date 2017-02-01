import re
import collections
from operator import itemgetter
totalCount = 0

with open('roomCodes.txt') as txtfile:
    for possibleRoom in txtfile:
        firstChunk = possibleRoom.split('[')[0]
        theRest = possibleRoom.split('[')[1] #[2]?
        firstChunk = firstChunk.replace("-","")
        theRest = theRest.split("]")[0]
        charsToSort = re.split('(\d+)', firstChunk)[0]
        sectorID = re.split('(\d+)', firstChunk)[1]
        letters = collections.Counter(charsToSort).most_common()
        
        letters = sorted(letters, key = itemgetter(0))
        letters = sorted(letters, key = itemgetter(1), reverse = True)

        letterIndex = 0
        finalLetters = ""
        while letterIndex < 5:
            finalLetters += letters[letterIndex][0]
            letterIndex += 1

        if theRest == finalLetters:
            totalCount += int(sectorID)

    print(totalCount)