def main():
	opcodeProgrammInput = open("inputDay5.txt", "r")
	for line in opcodeProgrammInput:
		opcodeProgramm = [int(code) for code in line.split(",")]

	opcodeProgrammInput.close()

	runOpcodeProgramm(opcodeProgramm)
	print(opcodeProgramm)

def runOpcodeProgramm(opcodeProgramm):
	position = 0

	while(position <= len(opcodeProgramm)):
		currentOpcode = str(opcodeProgramm[position])
		rightMostDigit = int(currentOpcode[len(currentOpcode) - 1])
		print(rightMostDigit)

		if rightMostDigit == 1:
			position = additionMode(position, opcodeProgramm)

		elif rightMostDigit == 2:
			position = multiplicationMode(position, opcodeProgramm)

		elif rightMostDigit == 3:
			position = inputMode(position, opcodeProgramm)

		elif currentOpcode == 4:
			position = outputMode(position, opcodeProgramm)

		elif currentOpcode == 99:
			print("End Point reached!")
			break

		else:
			print("No vaild Opcode "+ str(currentOpcode) + " on position: " + str(position))
			break

	return opcodeProgramm

def additionMode(position, opcodeProgramm):
	opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[opcodeProgramm[position+1]] + opcodeProgramm[opcodeProgramm[position+2]]
	position += 4
	return position

def multiplicationMode(position, opcodeProgramm):
	opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[opcodeProgramm[position+1]] * opcodeProgramm[opcodeProgramm[position+2]]
	position += 4
	return position

def inputMode(position, opcodeProgramm):
	opcodeProgramm[opcodeProgramm[position+1]]= 1
	position += 2
	return position

def outputMode(position, opcodeProgramm):
	outputValue = opcodeProgramm[opcodeProgramm[position+1]]
	position += 2
	print(outputValue)
	return position

main()