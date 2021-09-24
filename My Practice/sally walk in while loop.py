import random
totalsteps = int()
sally = "@_'-'"
days = 1
# loop to make sally walk
for count in range(0, 5):
    # create sally
    totalsteps = totalsteps + random.randint(1,5)
    steps = sally * totalsteps
print (totalsteps)
print (steps)
