with open ("input.txt", "r") as myfile:
	data=myfile.read().replace('\n', '')

Etage = 0
Position = 0
Stop = 0
for i in range(0,len(data)):
	if data[i]=='(':
		Etage = Etage +1
	elif data[i]==')':
		Etage = Etage -1
        if Stop == 0:
            if Etage == -1:
                Position= i+1
                print 'Santa reaches Floor -1 first at position', Position
                Stop = 1

