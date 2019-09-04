from random import choice #imports a random choice
list2d = [[choice((0,1)) for x in range(8)] for y in range(8)] #the random choice is either 0 or 1; there are 8 x values and 8 y values
for x in range(8): 
    print(list2d[x])
