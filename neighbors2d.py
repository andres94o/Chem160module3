from random import choice
n = 175 #size of the grid
count = 0 #this will be used to count the number of neighbors a cell has
nocc = 0 #keeping track of how many cells out of the entire grid have a cell in it
list2d = [[choice((0, 1)) for x in range(n)] for y in range(n)] #the list comprehension, x by y grid; a number (choice) will be chosen between 1 and 0 and the grid will be randomly filled
for x in range(1, n-1): #these for loops and if loops will loop over the grid created; find the occupied cells and count the neighbors
    for y in range(1, n-1): #these for loops will go through every cell in the center of the grid
        if list2d[x][y] == 1: #this chekcs to see of the cell is occupied; and if it is it will go into this if loop
            nocc += 1 # a number +1 will be added to occupied cells
            neighbor = list2d[x - 1][y] + list2d[x + 1][y] + list2d[x][y - 1] + list2d[x][y + 1] #this will add up the number of neighbors the cell has
            if neighbor > 2: 
                count += 1
print("Fraction with more than 2 neighbors:", count/nocc)
