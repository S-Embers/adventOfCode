class Planet():
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.children = []

	def totalOrbits(self):
		if self.parent == None:
			return 0

		return 1 + self.parent.totalOrbits()

def main():
	planetList = registerPlanets()

	orbitCount = 0
	for planet in planetList:
		orbitCount += planet.totalOrbits()
	
	print(orbitCount)

	sharedParent = searchForFirstSharedOrbit("YOU","SAN",planetList)

def registerPlanets():
	inputOrbits = open("input_Day6.txt", "r")
	planets = []

	for orbit in inputOrbits:
		bodyName, planetName = orbit.rstrip().split(")")
		satelite = None
		body = None
		for p in planets:
			if planetName == p.name:
				satelite = p
			if bodyName == p.name:
				body = p

		if satelite != None and body != None:
			satelite.parent = body
			body.children.append(satelite)
		elif satelite != None and body == None:
			body = Planet(bodyName, None)
			body.children.append(satelite)
			satelite.parent = body
			planets.append(body)
		elif satelite == None and body != None:
			satelite = Planet(planetName, body)
			body.children.append(satelite)
			planets.append(satelite)
		elif satelite == None and body == None:
			body = Planet(bodyName, None)
			satelite = Planet(planetName, body)
			body.children.append(satelite)
			planets.append(body)
			planets.append(satelite)

	inputOrbits.close()
	return planets

def searchForFirstSharedOrbit(startPlanet,endPlanet,planetList):
	start = None
	end = None

	for planet in planetList:
		if planet.name == startPlanet:
			start = planet
		if planet.name == endPlanet:
			end = planet

	startPlanetParents = set()
	endPlanetParents = set()
	startPlanetParents = getAllParents(start, startPlanetParents)
	endPlanetParents = getAllParents(end, endPlanetParents)

	sharedParents = startPlanetParents&endPlanetParents
	print(sharedParents)


def getAllParents(childPlanet, allParents):
	
	if childPlanet.parent != None:
		allParents = getAllParents(childPlanet.parent, allParents)
		allParents.add(childPlanet.parent)

	return allParents



main()