# This whole program could probably have been written without as many if-statements if I had used a data structure
# + had noticed that to win you had to choose the object that was (enemyChoice + 2) % 3

def CalculateScore(line):
	result = 0

	splitLine = line.split(" ")
	enemyChoice = splitLine[0]
	response = splitLine[1].strip()

	if response == "X":
		result += 1
	if response == "Y":
		result += 2
	if response == "Z":
		result += 3

	# a win
	if (response == "X" and enemyChoice == "C") or (response == "Y" and enemyChoice == "A") or (response == "Z" and enemyChoice == "B"):
		result += 6

	# a draw
	if (response == "X" and enemyChoice == "A") or (response == "Y" and enemyChoice == "B") or (response == "Z" and enemyChoice == "C"):
		result += 3

	# a loss
	# if (response == "X" and enemyChoice == "A") or (response == "Y" and enemyChoice == "B") or (response == "Z" and enemyChoice == "C"):
	# 	result += 3

	return result



def secondPartCalculate(line):
	result = 0

	splitLine = line.split(" ")
	enemyChoice = splitLine[0]
	response = splitLine[1].strip()

	if response == "X":
		result += 0
	if response == "Y":
		result += 3
	if response == "Z":
		result += 6


	if response == "X":
		if enemyChoice == "A":
			result += 3
		if enemyChoice == "B":
			result += 1
		if enemyChoice == "C":
			result += 2

	if response == "Y":
		if enemyChoice == "A":
			result += 1
		if enemyChoice == "B":
			result += 2
		if enemyChoice == "C":
			result += 3

	if response == "Z":
		if enemyChoice == "A":
			result += 2
		if enemyChoice == "B":
			result += 3
		if enemyChoice == "C":
			result += 1

	return result

def partOne():
	with open("input.txt", "r") as file:
		score = 0
		for line in file:
			score = score + CalculateScore(line)
	
		print(score)


def partTwo():
	with open("input.txt", "r") as file:
		score = 0
		for line in file:
			score = score + secondPartCalculate(line)
	
		print(score)

partTwo()