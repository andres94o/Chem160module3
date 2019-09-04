from random import choice
side = 4 #number of squares, 1-D
x = 0 #x is initally zero
for i in range(30): # 30 steps
    x += choice((-1, 1)) # a value for x will be chosen, randomly, between 1 and -1
    if x < 0: #if x is zero and the random number chosen is -1, x will be the #3, because it has 4 squres but it starts at zero
        x = side - 1 #this will make it equal 3
    if x == side: #if x is 3, the last square, and the random number chosen is +1, then x will become zero
        x = 0
    print(x)
