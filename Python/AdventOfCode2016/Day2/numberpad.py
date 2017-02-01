
def tryMakeMove(char, x, y):
    tempX = x
    tempY = y

    if char == 'U':
        tempY -= 1
        if tempY > -1:
            y = tempY
    if char == 'D':
        tempY += 1
        if tempY < 3:
            y = tempY
    if char == 'L':
        tempX -= 1
        if tempX > -1:
            x = tempX
    if char == 'R':
        tempX += 1
        if tempX < 3:
            x = tempX
    return x,y

with open('codedNumber.txt') as txtfile:
     for line in txtfile:
        numChars = len(line)
        index = 0
        x = 1   #this x, y, combo corresponds to 5 on the numberpad
        y = 1
        while index < numChars:
            char = line[index]
            x,y = tryMakeMove(char, x, y)
            index += 1
        print((3*y)+x+1)