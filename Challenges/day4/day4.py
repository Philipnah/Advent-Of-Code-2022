
def foldNumberOut(elfStart, elfEnd):
	list = []
	i = int(elfStart)

	while i <= int(elfEnd):
		list.append(i)
		i += 1

	return list

def partOne():
	with open("/Users/philip/Desktop/Git/Advent-Of-Code-2022/Challenges/day4/input.txt", "r") as file:
		result = 0

		for line in file:
			elfA = line.split(",")[0]
			elfB = line.split(",")[1]

			elfAStart = elfA.split("-")[0].strip()
			elfAEnd = elfA.split("-")[1].strip()
			
			elfBStart = elfB.split("-")[0].strip()
			elfBEnd = elfB.split("-")[1].strip()

			# Alist = foldNumberOut(elfAStart, elfAEnd)
			# Blist = foldNumberOut(elfBStart, elfBEnd)

			# j = 0
			# for i in Alist:
			# 	if i in Blist:
			# 		j += 1
			# if j == len(Alist) - 1:
			# 	result += 1

			# j = 0
			# for i in Blist:
			# 	if i in Alist:
			# 		j += 1
			# if j == len(Blist) - 1:
			# 	result += 1

			# if elfAStart <= elfBStart and elfAEnd >= elfBEnd:
			# 	result += 1
			# else:
			# 	if elfBStart <= elfAStart and elfBEnd >= elfAEnd:
			# 		result += 1
			if (elfBStart >= elfAStart and elfAEnd >= elfBEnd) or (elfAStart >= elfBStart and elfBEnd >= elfAEnd):
				result += 1

			

		print(result)

partOne()