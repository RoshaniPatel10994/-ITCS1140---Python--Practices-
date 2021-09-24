#Variables
months = 0.0
weeks = 0.0
weekly_savings = 0.0
monthly_saving = 0.0
total_saving = 0.0

# Outer loop to determin how nuch snow fell in total
for week in range(1,6):
    # Inner loop determine the monthly total
    for days in range(1,4):
        user = float(input("Weekly Savings: "))
        weekly_savings = weekly_savings + user
    print("Monthly Savings:", weekly_savings)
    total_saving = total_saving + weekly_savings
    weekly_savings = 0.0
    print("Total Savings:", total_saving)
    print()
    

