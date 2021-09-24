
#2/24/2020
import random
#Declare Variables
guess = int()
game_number = int()
user_answer = str()
counter = int()
user_answer = "Y"

# Loop to play a Game
while user_answer == "Y":
    game_number = random.randint(1,50)

    # For Loop
    for counter in range(0, 3):
        #ask user for their gues
        guess = int(input("Enter your guess:  "))
        #Determine if the user guessed the number
        if guess == game_number:
            print("Congratulations You Won!")
            break
        elif guess < game_number:
            print("Guess a Little Higher")
        else:
            print("Guess a Little Lower")
        #end if
        #End loop
        #Displaying the message if the user did not win
    if guess != game_number:
        print("Sorry you did not win.")
    #end if
        print("The number was: ",game_number)
        user_answer = input("Did you want to continue (Y or N):"  )
