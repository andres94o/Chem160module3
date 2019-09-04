from random import choice #imports a random choice (number)
counter = 0
while counter < 100: #while the counter is less than 100 perform this while loop
    print(counter) #prints the number associated with counter
    counter += choice(range(10)) #a random choice is made between 0-9, and this is added to counter

pop = 100 #population is initally 100
while 1: #while this is 1, which is always true because pop is 100, perform this while loop
    pop = pop * 1.89 #multiply pop by 1.89
    if pop > 1000: #if the pop gets greater than 1000, break the loop and print the population
        break
print(" The final population is ", pop)
