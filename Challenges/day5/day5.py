# [N]             [R]             [C]
# [T] [J]         [S] [J]         [N]
# [B] [Z]     [H] [M] [Z]         [D]
# [S] [P]     [G] [L] [H] [Z]     [T]
# [Q] [D]     [F] [D] [V] [L] [S] [M]
# [H] [F] [V] [J] [C] [W] [P] [W] [L]
# [G] [S] [H] [Z] [Z] [T] [F] [V] [H]
# [R] [H] [Z] [M] [T] [M] [T] [Q] [W]
#  1   2   3   4   5   6   7   8   9 

# TODO strip every element of the combined list


def split3(string):
	return [string[i:i+4] for i in range(0, len(string), 4)]

def getCombinedList():
	combinedList = []

	with open("Challenges/day5/input.txt", "r") as file:
		for line in file:
			if "[" in line:
				combinedList += split3(line)
			
	return combinedList

def cleanList(list):
	return [list[i].strip(" []\n") for i in range(0, len(list))]

def getColumns():
	cleanCombinedList = cleanList(getCombinedList())
	
	# creating the columns list
	columns = []
	for i in range(0, 9):
		columns.append([])

	# writing the columns list
	for i in range(0, len(cleanCombinedList)):
		if cleanCombinedList[i] != "":
			columns[i % 9].append(cleanCombinedList[i])

	return columns

def partTwoMove(amount, fromColumn, toColumn, columns):
	temp = []

	for i in range(0, amount):
		temp.append(columns[fromColumn][0])
		columns[fromColumn].pop(0)

	columns[toColumn] = temp + columns[toColumn]

def move(amount, fromColumn, toColumn, columns):
	for i in range(0, amount):
		columns[toColumn] = [columns[fromColumn][0]] + columns[toColumn]
		columns[fromColumn].pop(0)


def main():
	columns = getColumns()

	with open("Challenges/day5/input.txt", "r") as file:
		for line in file:
			if "move" in line:
				splitLine = line.split(" ")
				move(int(splitLine[1]), int(splitLine[3]) - 1, int(splitLine[5]) - 1, columns)
	
	for column in columns:
		print(column[0], end="")
		
	print("\n")
			
def partTwo():
	columns = getColumns()

	with open("Challenges/day5/input.txt", "r") as file:
		for line in file:
			if "move" in line:
				splitLine = line.split(" ")
				partTwoMove(int(splitLine[1]), int(splitLine[3]) - 1, int(splitLine[5]) - 1, columns)
	
	for column in columns:
		print(column[0], end="")
	
	print("\n")

main()
partTwo()