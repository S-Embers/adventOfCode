import re

def main():
	#wireList = []

	#wireInput = open("day3.txt", "r")
	#for wire in wireInput:
	#	wireList.append(wire)
	#wireInput.close

	#wire1 = wireList[0].split(",")
	#wire2 = wireList[1].split(",")

	wireList1 ="R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
	wireList2 ="U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

	wire1 = wireList1.split(",")
	wire2 = wireList2.split(",")

	wirePath1 = buildWire(wire1)
	wirePath2 = buildWire(wire2)

	intersections = getWireIntersections(wirePath1, wirePath2)
	print(intersections)
	print(smallestManhattenDistance(intersections))

def getWireIntersections(wire1, wire2):
	intersections = []
	for pathPoint1 in wire1:
		for pathPoint2 in wire2:
			if pathPoint1[0] == pathPoint2[0]:
				if pathPoint1[1] == pathPoint2[1]:
					intersections.append(pathPoint1)

	return intersections

def smallestManhattenDistance(intersections):
	manhattenDistances = []
	for intersection in intersections:
		manhattenDistances.append(calculateManhattenDistance(intersection))

	manhattenDistances.sort()
	print(manhattenDistances)
	return manhattenDistances[0]

def buildWire(wire):
	wirePath = []
	wireX = 0
	wireY = 0

	for direction in wire:
		directionParts = re.split("(\d+)", direction)

		if directionParts[0] == "L":
			for path in range(0,int(directionParts[1])):
				wireX -= 1
				pathPoint = [wireX, wireY]
				wirePath.append(pathPoint)
				
		elif directionParts[0] == "R":
			for path in range(0,int(directionParts[1])):
				wireX += 1
				pathPoint = [wireX, wireY]
				wirePath.append(pathPoint)
				
		elif directionParts[0] == "U":
			for path in range(0,int(directionParts[1])):
				wireY += 1
				pathPoint = [wireX, wireY]
				wirePath.append(pathPoint)
				
		elif directionParts[0] == "D":
			for path in range(0,int(directionParts[1])):
				wireY -= 1
				pathPoint = [wireX, wireY]
				wirePath.append(pathPoint)			
		else:
			print("No Valid orientation")

	print("finished!")
	return wirePath

def calculateManhattenDistance(point):
	return point[0] + point[1]


main()