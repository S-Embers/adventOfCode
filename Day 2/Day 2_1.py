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
			print("No vaild Opcode "+ currentOpcode + " on position: " + position)
			break

	print(opcodeProgramm)
	return opcodeProgramm[0]


opcodeProgrammInput = open("inputDay2_1.txt", "r")
for line in opcodeProgrammInput:
	opcodeProgramm = [int(code) for code in line.split(",")]

opcodeProgrammInput.close()

opcodeProgramm[1] = 12
opcodeProgramm[2] = 2

print(runOpcodeProgramm(opcodeProgramm))