
# Declare variables
letterGrade = str()
score = int()
score = int(input("Enter your test score:  "))

# If and else statment
if score <= 70:
    letterGrade = "C"
    print(letterGrade)
elif score <= 80:
    letterGrade = "B"
    print(letterGrade)
elif score <= 90:
    letterGrade = "A"
    print(letterGrade)
    # Print
print("Your Grade is: " , letterGrade)
