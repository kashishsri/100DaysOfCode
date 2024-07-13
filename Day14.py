from Day14_art import logo, vs
from Day14_data import data
import random
import os


score = 0
game_on = True
account_b = random.choice(data)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def format_data(account):
    """ Takes the account data and returns into printable format """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_desc}, from {account_country}.")

def check_answer(guess, a_follower, b_follower):
    ## Uses if statement to check if user is correct
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


while game_on:# Make game repeatable
    # Generate a random account from data
    account_a = account_b
    account_b = random.choice(data)
    ## making account at position B become the next account at position A
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user to guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check user is correct
    ## Get follower count of each account
    a_account_follower = account_a["follower_count"]
    b_account_follower = account_b["follower_count"]

    correct = check_answer(guess, a_account_follower, b_account_follower)
    ## Clear screen between rounds
    clear_console()
    # Display art
    print(logo)
    # Give user feedback
    if correct:
        # Score keeping
        score += 1
        print(f"\nYou're right!. Current score: {score}\n")
    else:
        game_on = False
        print(f"\nSorry that's wrong. Final score: {score}")

