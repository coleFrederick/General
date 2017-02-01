#create dictionary or 2d array of numberPad layout
numPad = {(0,0):'X',(1,0):'X', (2,0):'1', (3,0):'X', (4,0):'X',
            (0,1):'X',(1,1):'2', (2,1):'3', (3,1):'4', (4,1):'X',
            (0,2):'5',(1,2):'6', (2,2):'7', (3,2):'8', (4,2):'9',
            (0,3):'X',(1,3):'A', (2,3):'B', (3,3):'C', (4,3):'X',
            (0,4):'X',(1,4):'X', (2,4):'D', (3,4):'X', (4,4):'X'}


def tryMakeMove(char, x, y):
    tempX = x
    tempY = y

    if char == 'U':
        tempY -= 1
        if numPad.get((x,tempY), 'X') != 'X' :
            y = tempY
    if char == 'D':
        tempY += 1
        if numPad.get((x,tempY), 'X') != 'X' :
            y = tempY
    if char == 'L':
        tempX -= 1
        if numPad.get((tempX,y), 'X') != 'X' :
            x = tempX
    if char == 'R':
        tempX += 1
        if numPad.get((tempX,y), 'X') != 'X' :
            x = tempX

    return x,y

with open('codedNumber.txt') as txtfile:
     for line in txtfile:
        numChars = len(line)
        index = 0
        x = 0   #this x, y, combo corresponds to 5 on the numberpad
        y = 2
        while index < numChars:
            char = line[index]
            x,y = tryMakeMove(char, x, y)
            index += 1
        print(numPad.get((x,y)))