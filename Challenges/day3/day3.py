def CalculatePriority(char):
	offset = 96

	if ord(char) < 97:
		return ord(char) + (52+6) - 96
	else:
		return ord(char) - 96

def partOne():
	with open("input.txt", "r") as file:
		sum = 0

		for line in file:
			firstPart = line[:(len(line)//2)]
			secondPart = line[(len(line)//2):]

			for char in firstPart:
				if char in secondPart:
					sum += CalculatePriority(char)
					break
		print(sum)


def partTwo():
	with open("input.txt", "r") as file:
		sum = 0
		prevLine = ""
		prevPrevLine = ""

		i = 1

		for line in file:
			
			if i%3 == 0 and i != 0:
				for char in prevPrevLine:
					if char in prevLine and char in line:
						sum += CalculatePriority(char)
						break

			i += 1 

			prevPrevLine = prevLine
			prevLine = line



			
		print(sum)




partOne()
partTwo()