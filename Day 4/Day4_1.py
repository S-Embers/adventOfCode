def main():
	targetRange = [152085, 670283]
	validCombinations = []

	combination = targetRange[0]

	for _ in range(targetRange[1]-targetRange[0]):
		if isAscending(combination):
			if hasSameNeighbours(combination):
				validCombinations.append(combination)
		combination += 1

	print(len(validCombinations))

def hasSameNeighbours(combination):
	strCombination = str(combination)

	if strCombination[1] == strCombination[0] or strCombination[1] == strCombination[2] or strCombination[2] == strCombination[3] or strCombination[4] == strCombination[3] or strCombination[4] == strCombination[5]:
		return True
	else:
		return False

def isAscending(combination):
	strCombination = str(combination)

	if strCombination[0] <= strCombination[1] and strCombination[1] <= strCombination[2] and strCombination[2] <= strCombination[3] and strCombination[3] <= strCombination[4] and strCombination[4] <= strCombination[5]:
		return True
	else:
		return False


main()