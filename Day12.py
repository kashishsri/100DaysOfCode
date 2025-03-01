#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from Day12_art import logo
import random

print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, answer, turns):
    if user_guess > answer:
        print("Too high")
        return turns-1
    elif user_guess < answer:
        print("Too low")
        return turns-1
    else:
        print(f"You got it!. The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    # print(f"Answer is {answer}")

    turns = set_difficulty()

    # To keep guessing
    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess : "))
        turns = check_answer(user_guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses. You lose.")
            return
        elif user_guess != answer:
            print("Guess Again.")




game()

