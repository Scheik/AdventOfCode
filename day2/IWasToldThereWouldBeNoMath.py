with open ("input.txt", "r") as myfile:
	for line in myfile:
		dimension = line.split("x")
		l = dimension[0]
		w = dimension[1]
		h = dimension[2]
		print l
		print w
		print h


