N = 33 #the inital number
steps = 0 #steps initally set at zero
while N != 1: #as long as N does not equal 1 perform this while loop
    print(N) #print the number associated with N
    steps += 1 #after it gets printed add +1
    if N%2 == 0: #if N is divisible by 2 and leaves no remainder, go into this if statement
        N = N//2 #N will be divided by 2
    else: #if a remiander is left over, go into the else statement instead
        N = (3 * N) + 1
print("steps =", steps) #prints the number of steps it takes to get to number 1
