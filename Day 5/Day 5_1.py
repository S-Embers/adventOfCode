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

		if rightMostDigit == 1:
			position = additionMode(position, opcodeProgramm)

		elif rightMostDigit == 2:
			position = multiplicationMode(position, opcodeProgramm)

		elif rightMostDigit == 3:
			position = inputMode(position, opcodeProgramm)

		elif rightMostDigit == 4:
			position = outputMode(position, opcodeProgramm)

		elif opcodeProgramm[position] == 99:
			print("End Point reached!")
			break

		else:
			print("No vaild Opcode "+ str(currentOpcode) + " on position: " + str(position))
			break

	return opcodeProgramm

def additionMode(position, opcodeProgramm):
	opcodeInstruction = str(opcodeProgramm[position])

	if len(opcodeInstruction) == 1:
		opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[opcodeProgramm[position+1]] + opcodeProgramm[opcodeProgramm[position+2]]
		position += 4
		return position
	elif len(opcodeInstruction) == 3:
		opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[position+1] + opcodeProgramm[opcodeProgramm[position+2]]
		position += 4
		return position
	elif len(opcodeInstruction) == 4:
		if int(opcodeInstruction[0]) == 1 and int(opcodeInstruction[1]) == 0: 
			opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[opcodeProgramm[position+1]] + opcodeProgramm[position+2]
			position += 4
			return position
		elif int(opcodeInstruction[0]) == 1 and int(opcodeInstruction[1]) == 1:
			opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[position+1] + opcodeProgramm[position+2]
			position += 4
			return position
		else:
			print("no vailid code")
			opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[position+1] + opcodeProgramm[position+2]
			position += 4
			return position
	else:
		return position+1


def multiplicationMode(position, opcodeProgramm):
	opcodeInstruction = str(opcodeProgramm[position])

	if len(opcodeInstruction) == 1:
		opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[opcodeProgramm[position+1]] * opcodeProgramm[opcodeProgramm[position+2]]
		position += 4
		return position
	elif len(opcodeInstruction) == 3:
		opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[position+1] * opcodeProgramm[opcodeProgramm[position+2]]
		position += 4
		return position
	elif len(opcodeInstruction) == 4:
		if int(opcodeInstruction[0]) == 1 and int(opcodeInstruction[1]) == 0: 
			opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[opcodeProgramm[position+1]] * opcodeProgramm[position+2]
			position += 4
			return position
		elif int(opcodeInstruction[0]) == 1 and int(opcodeInstruction[1]) == 1: 
			opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[position+1] * opcodeProgramm[position+2]
			position += 4
			return position
		else:
			print("no vailid code")
			position += 4
			return position
	else:
		return position+1

def inputMode(position, opcodeProgramm):
	opcodeProgramm[opcodeProgramm[position+1]]= 1
	position += 2
	return position

def outputMode(position, opcodeProgramm):
	opcodeInstruction = str(opcodeProgramm[position])

	if len(opcodeInstruction) == 1:
		outputValue = opcodeProgramm[opcodeProgramm[position+1]]
		position += 2
		print(outputValue)
		return position
	elif len(opcodeInstruction) == 3:
		outputValue = opcodeProgramm[position+1]
		position += 2
		print(outputValue)
		return position
	else:
		return position+1
	

main()