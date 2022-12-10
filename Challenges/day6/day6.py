def main(amountOfCharacters):
	with open("Challenges/day6/input.txt", "r") as file:
		allCharacters = file.read()
		characterBuffer = []

		for counter in range(0, len(allCharacters)):
			if len(characterBuffer) >= amountOfCharacters:
				if checkAllCharacters(characterBuffer):
					print(counter)
					break
				else:
					characterBuffer = shiftArray(characterBuffer)
			
			characterBuffer.append(allCharacters[counter])
				

def shiftArray(array):
	returnedArray = []
	
	for i in range(1, len(array)):
		returnedArray.append(array[i])
	
	return returnedArray

def checkAllCharacters(array):
	for firstCount in range(0, len(array)):
		for secondCount in range(firstCount + 1, len(array)):
			if array[firstCount] == array[secondCount]:
				return False
	
	return True


print("\nAnswer part 1: ")
main(4)

print("\nAnswer part 2: ")
main(14)