print("Welcome to Treasure Islnd.\nYour mission is to find the treasure.")
path = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\". \n").lower()

if path == "left":
    # Continue in the game.
    sec_step = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if sec_step == "wait":
        #  Continue in the game.
        third_step = input("You've arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if third_step == "red":
            print("It's a room full of fire. Game Over.")
        elif third_step == "blue":
            print("You entered a room full of beasts. Game Over.")
        elif third_step == "yellow":
            print("You found the treasure!. You Win!")
        else:
            print("You chose a door that doesn't exists. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
