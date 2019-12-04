def calculateFuelAmount(mass):
	fuelAmount = int(mass/3) - 2

	if fuelAmount < 0:
		return 0

	elif fuelAmount > 0:
		fuelAmount += calculateFuelAmount(fuelAmount)

	return fuelAmount

modulMassesInput = open("inputDay1_1.txt", "r")
totalAmountOfFuel = 0

for modulMass in modulMassesInput:
	totalAmountOfFuel = totalAmountOfFuel + calculateFuelAmount(int(modulMass))

modulMassesInput.close()

print(totalAmountOfFuel)