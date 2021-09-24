##Let’s create a program to measure how many cans of soup we have collected
##for food drive that will take place on Friday, Saturday and Sunday for 2 weeks.
##Our program needs to ask the user for the number of cans they are collecting each of those days.
##It needs to produce a total for those 3 days and then a total after the 2 weeks.

# variables
total_cans = int()
weekly_cans = int()
daily_cans = int()
days = int()
weeks = int()
#Outer loop keeping track of number of weeks

for weeks in range(1, 3):

    #Inner loop keeps track of days
    for days in range(1, 4):
        daily_cans = int(input("Enter total cans collected today:  "))
        weekly_cans = weekly_cans + daily_cans

    #end loop
    print("Total cans collected this week:  ", weekly_cans)

    total_cans = total_cans + weekly_cans

    print("Total cans collected for the entire drive:  ", total_cans)

    weekly_cans = 0
#end outer loop
