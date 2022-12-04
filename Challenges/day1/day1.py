import sys

def partOne():
	maxCalorieElf = 0
	currentElf = 0

	with open("input.txt", "r") as file:
		for line in file:
			if line == "\n":
				if currentElf > maxCalorieElf:
					maxCalorieElf = currentElf
				currentElf = 0
			else:
				currentElf = currentElf + int(line)
		
		print(maxCalorieElf)


def minElementIndex(array):
	minimum = sys.maxsize
	minIndex = 0
	for i in range(len(array)):
		if array[i] < minimum:
			minimum = array[i]
			minIndex = i

	return minIndex
		

def partTwo():
	maxCalorieElves = [0, 0, 0]
	currentElf = 0

	with open("input.txt", "r") as file:
		for line in file:
			if line == "\n":
				if currentElf > min(maxCalorieElves):
					maxCalorieElves[minElementIndex(maxCalorieElves)] = currentElf

				currentElf = 0
			else:
				currentElf = currentElf + int(line)
		
		sum = 0
		for elf in maxCalorieElves:
			sum = sum + elf
		
		print(sum)

partTwo()
