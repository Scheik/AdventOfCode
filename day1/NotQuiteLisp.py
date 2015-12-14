with open ("input.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

Etage = 0

for i in range(0,len(data)):
    if data[i]=='(':
        Etage = Etage +1
    elif data[i]==')':
        Etage = Etage -1


print Etage
