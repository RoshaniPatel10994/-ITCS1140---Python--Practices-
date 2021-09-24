# Variables
test_score= float()
total_score = float()
user = str()
ans = str()

# While loop
while user != "yes":

    # Ask the user
    test_score = float(input("Enter the test score:  "))
    total_score = total_score + test_score
    # Ask the user
    user = str(input("Do you want to quit entering scores (yes or no): "))
    # Print
    print("Your Total Score is: ",  total_score)
