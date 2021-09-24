#Variables
months = int()
weeks = int()
week_value = int()
month_total = int()
month_average = float()
total_inches = int()
ave_inches = float()


# Outer loop to determin how nuch snow fell in total
for months in range(1,6):
    # Inner loop determine the monthly total
    for weeks in range(1,5):
        week_value = int(input("Enter your weekly snow fell(in inches): "))
        # Accumulating
        month_total = month_total + week_value        
    #End foor loop
    month_average = month_total / weeks
    
    # Add Month total to total inches
    total_inches = total_inches+ month_total
    
    # Printout monthly total and average
    print()
    print("monthly total:\t", month_total)
    print("month average:\t", month_average)
    
    #Reset month total to start a new month
    month_total = 0
    
# End For
ave_inches = total_inches/months

#print out and average
print("Total snow fall:\t", total_inches)
print("Total average inches:\t", ave_inches)




    
   
