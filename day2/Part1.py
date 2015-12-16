summe = 0
with open ("input.txt", "r") as myfile:
    for line in myfile:
		dimension = line.split("x")
		l = int(dimension[0])
		w = int(dimension[1])
		h = int(dimension[2])
                surface = 2*l*w + 2*w*h + 2*h*l
                summe = summe + surface
                first_minimalst = min(l,h,w)
                if first_minimalst == l:
                    second_minimalst = min(h,w)
                elif first_minimalst == h:
                    second_minimalst = min(l,w)
                elif first_minimalst == w:
                    second_minimalst = min(l,h)
                summe = summe + (first_minimalst*second_minimalst)
print summe
