X = Y = 0
visited = [(0,0)]
unique_visited = 1

with open ('input.txt') as myfile:
    for char in myfile.read():
        if char =='^':
            Y += 1
        elif char =='v':
            Y -= 1
        elif char == '<':
            X -= 1
        elif char == '>':
            X += 1
        if (X, Y) not in visited:
            unique_visited += 1
            visited.append((X, Y))
print unique_visited
