
import random
randomnum = int()
ally = str()
days = int()
totalsteps = int()
steps = str()
# variable

days = 1
sally ="0_'-'"

# loop to make sally walk

while days <=5:
    # Generate random num
    randomnum = random.randint(1, 5)
    # create sally
    steps = sally* randomnum
    # keeps track of sally steps
    totalsteps = totalsteps + randomnum
    print(steps, end=' ')
# increment days
    days = days+ 1
# end loop
#print()
#print()
print("sally waked", totalsteps, "steps")

  
