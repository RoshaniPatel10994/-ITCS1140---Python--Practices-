# Variables
user_continue = str()
item = str()

# While loop
while user_continue != "Q":
    item = input("Enter a shopping list item:  ")
    # Print the item
    print(item)
    user_continue = input("Enter Q to quit:  ")
