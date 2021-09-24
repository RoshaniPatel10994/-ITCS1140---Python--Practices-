#This program will collect rocks every day for 2 weeks.
#The program needs to print out a weekly total and a total after two weeks.

#Declare variables

rocks_day = int()
rocks_week = int()
rocks_total = int()
days = 1
week = 1

#Get total number of rocks
while week <=2:
    while days <=7:
        #Ask uder for number of rocks collected today
        rocks_day = int(input("Enter the rocks you collected today: "))
        rocks_week = rocks_week + rocks_day
        days = days + 1
    #end while
    rocks_total = rocks_total + rocks_week
    print("You collected: ", rocks_week, "rocks this week")
   #rocks_week=0
    days = 1
    week = week+1
#End while
print("You collected: ", rocks_total)


