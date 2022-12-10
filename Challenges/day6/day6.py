def func():
	with open("/Users/philip/Desktop/Git/Advent-Of-Code-2022/Challenges/day6/input.txt", "r") as file:
		allCharacters = file.read()

		characterBuffer = []
		for i in range(0, len(allCharacters)):
			#print(characterBuffer)
			
			if len(characterBuffer) < 4:
				characterBuffer.append(allCharacters[i])
			else:
				if allCharacters[i] in characterBuffer:
					characterBuffer = shiftArray(characterBuffer)
					characterBuffer.append(allCharacters[i])
				else:
					if checkAllCharacters(characterBuffer):
						print(i)
						print(allCharacters[i])
						print(characterBuffer)
						break
					else:
						characterBuffer = shiftArray(characterBuffer)
						characterBuffer.append(allCharacters[i])
				



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

func()