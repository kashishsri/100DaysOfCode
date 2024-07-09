# User Defined Function to clear console output
import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

from Day9_art import logo
print(logo)

print("Welcome to the Secret Auction program.")

bidders_details = {}
game_on = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] # This gives us the value of the key bidder e.g. bidder = "John" and value = $45
        if highest_bid < bid_amount:
            highest_bid = bid_amount
            winner = bidder # this sets key as winner e.g. winner = "John" which is the key bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while game_on:
    user_name = input("What is yout name? : ")
    user_bid = int(input("What's your bid? : $"))
    bidders_details[user_name] = user_bid

    user_choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if user_choice == 'yes':
        clear_console()
    else:
        game_on = False
        find_highest_bidder(bidding_record=bidders_details)
        

