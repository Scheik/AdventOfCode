X_Santa = Y_Santa = X_Robo = Y_Robo = 0
visited = visited_Santa = visited_Robo = [(0,0)]
unique_visited = 1
santa_turn = True

with open ('input.txt') as myfile:
    for char in myfile.read():
        if santa_turn == True:
            if char == '^':
                Y_Santa += 1
            elif char == 'v':
                Y_Santa -= 1
            elif char == '<':
                X_Santa -= 1
            elif char == '>':
                X_Santa += 1
            if ((X_Santa, Y_Santa) not in visited_Santa) and ((X_Santa, Y_Santa) not in visited_Robo):
                unique_visited += 1
                visited_Santa.append((X_Santa, Y_Santa))
            
        if santa_turn == False:
            if char == '^':
                Y_Robo += 1
            elif char == 'v':
                Y_Robo -= 1
            elif char == '<':
                X_Robo -= 1
            elif char == '>':
                X_Robo += 1
            if ((X_Robo, Y_Robo) not in visited_Robo) and ((X_Robo, Y_Robo) not in visited_Santa):
                unique_visited += 1
                visited_Robo.append((X_Robo, Y_Robo))
        
        santa_turn = not santa_turn

print unique_visited
