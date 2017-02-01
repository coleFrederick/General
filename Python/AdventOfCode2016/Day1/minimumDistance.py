import csv

#directions = Enum('N', 'E', 'S', 'W')

newDirection = 0 #start facing N

verticalMovement = 0
horizontalMovement = 0

with open('directionsData.csv', 'rb') as csvfile:
     filereader = csv.reader(csvfile)
     for row in filereader:
		members = len(row)
		index = 0
		while index < members:
			member = row[index]
			cleanMember = member.strip()
			numSteps = int(cleanMember[1:])
			if cleanMember[0] == 'L':
				newDirection = newDirection - 1
			else:
				newDirection = newDirection + 1

			newDirection = (newDirection + 4)%4
			if newDirection == 0:
				verticalMovement = verticalMovement + numSteps
			if newDirection == 1:
				horizontalMovement = horizontalMovement + numSteps
			if newDirection == 2:
				verticalMovement = verticalMovement - numSteps
			if newDirection == 3:
				horizontalMovement = horizontalMovement - numSteps

			index = index + 1

print("You are ", verticalMovement, " blocks north and ", horizontalMovement, " blocks east")
print("You are ", abs(verticalMovement + horizontalMovement), " blocks away")