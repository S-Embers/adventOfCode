
def calculateFuelAmount(mass):
	fuelAmount = int(mass/3) - 2
	return fuelAmount

modulMassesInput = open("inputDay1_1.txt", "r")
totalAmountOfFuel = 0

for modulMass in modulMassesInput:
	totalAmountOfFuel = totalAmountOfFuel + calculateFuelAmount(int(modulMass))

modulMassesInput.close()
print(totalAmountOfFuel)