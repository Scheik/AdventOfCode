summe = 0
with open ("input.txt", "r") as myfile:
    for line in myfile:
                dimension = line.split("x")
                l = int(dimension[0])
                w = int(dimension[1])
                h = int(dimension[2])
                first_minimalst = min(l,h,w)
                if first_minimalst == l:
                    second_minimalst = min(h,w)
                elif first_minimalst == h:
                    second_minimalst = min(l,w)
                elif first_minimalst == w:
                    second_minimalst = min(l,h)
                summe = summe + (2*first_minimalst) + (2*second_minimalst)
		summe = summe + (l*w*h)
print summe
