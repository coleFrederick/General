import sys
import csv

#directions = Enum('N', 'E', 'S', 'W')
class Location:
	def __init__(self, x, y):
		self.x = x
		self.y = y

newDirection = 0 #start facing N

verticalMovement = 0
horizontalMovement = 0
existingIndex = 0
locationsToVisit = []
visitedLocations = []

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
				for index2 in range (1,numSteps+1):
					locationsToVisit.append(Location(horizontalMovement, verticalMovement+index2)) 			#need to keep track of each step taken, not in multi-block chunks
				verticalMovement = verticalMovement + numSteps
			if newDirection == 1:
				for index2 in range (1,numSteps+1):
					locationsToVisit.append(Location(horizontalMovement+index2, verticalMovement))
				horizontalMovement = horizontalMovement + numSteps
			if newDirection == 2:
				for index2 in range (1,numSteps+1):
					locationsToVisit.append(Location(horizontalMovement, verticalMovement-index2))
				verticalMovement = verticalMovement - numSteps
			if newDirection == 3:
				for index2 in range (1,numSteps+1):
					locationsToVisit.append(Location(horizontalMovement-index2, verticalMovement))
				horizontalMovement = horizontalMovement - numSteps

			for temp in locationsToVisit:
				for item in visitedLocations:
					if temp.x == item.x and temp.y == item.y:
						print("First repeat is at ", item.x, item.y)
						print("First repeat is ", abs(item.x + item.y), " blocks away")
						sys.exit()
				visitedLocations.append(temp)
			
			del locationsToVisit[:]
			index = index + 1

