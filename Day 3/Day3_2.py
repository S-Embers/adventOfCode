def main():
	wireList = []

	wireInput = open("day3.txt", "r")
	for wire in wireInput:
		wireList.append(wire)
	wireInput.close

	wire1 = wireList[0].split(",")
	wire2 = wireList[1].split(",")

	pointsOfWire1 = getPoints(wire1)
	pointsOfWire2 = getPoints(wire2)

	allIntersectionPoints = set(pointsOfWire1.keys())&set(pointsOfWire2.keys())
	shortestManhattenDistance = min([abs(x) + abs(y)] for (x,y) in allIntersectionPoints)
	fewestStepsToIntersection = min([pointsOfWire1[point] + pointsOfWire2[point] for point in allIntersectionPoints])
	print(shortestManhattenDistance)
	print(fewestStepsToIntersection)

def getPoints(wire):
	directionX = {"L": -1, "R": 1, "U": 0, "D": 0}
	directionY = {"L": 0, "R": 0, "U": 1, "D": -1}

	x = 0
	y = 0
	steps = 0

	pointSet = {}
	for cmd in wire:
		direction = cmd[0]
		length = int(cmd[1:])
		assert direction in ["L", "R", "U", "D"]
		for _ in range(length):
			x += directionX[direction]
			y += directionY[direction]
			steps += 1
			if (x,y) not in pointSet:
				pointSet[(x,y)] = steps

	return pointSet


main()