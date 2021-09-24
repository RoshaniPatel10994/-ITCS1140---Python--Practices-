import random
coin = int()
heads = int()
tails = int()
answer = str()
while answer != "Q":
    coin = random.randint(1,2)
    if coin == 1:
        heads = heads + 1
        print("Heads Win!\tScore:\t", heads)
    else:
        tails = tails + 1
        print("Tails Win!\tScore:\t", tails)
    #end if
        answer = input("Enter Q to quit")
#end loop
print("Heads score:\t", heads)
print("Tails score:\t", tails)
