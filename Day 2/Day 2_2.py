def runOpcodeProgramm(opcodeProgramm):
	position = 0

	while(position <= len(opcodeProgramm)):
		currentOpcode = opcodeProgramm[position]

		if currentOpcode == 1:
			opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[opcodeProgramm[position+1]] + opcodeProgramm[opcodeProgramm[position+2]]
			position += 4

		elif currentOpcode == 2:
			opcodeProgramm[opcodeProgramm[position+3]] = opcodeProgramm[opcodeProgramm[position+1]] * opcodeProgramm[opcodeProgramm[position+2]]
			position += 4

		elif currentOpcode == 99:
			print("End Point reached!")
			break

		else:
			print("No vaild Opcode "+ str(currentOpcode) + " on position: " + str(position))
			break

	return opcodeProgramm[0]

def outputSearch(outputNumber, opcodeProgramm):
	canidatesFound = False

	for noun in range(0,100):
		for verb in range(0,100):
			resetOpcode = opcodeProgramm[:]
			resetOpcode[1] = noun
			resetOpcode[2] = verb
			if outputNumber == runOpcodeProgramm(resetOpcode):
				print("Canidates Found!")
				return noun, verb

opcodeProgrammInput = open("inputDay2_1.txt", "r")
for line in opcodeProgrammInput:
	myOpcodeProgramm = [int(code) for code in line.split(",")]

opcodeProgrammInput.close()

noun, verb = outputSearch(19690720, myOpcodeProgramm)
endCode = 100 * noun + verb
print("With noun " + str(noun) + " and verb " + str(verb) + " the Endcode is " + str(endCode))