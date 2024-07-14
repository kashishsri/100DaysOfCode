MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 4: Check resources sufficient?
def check_resources(order_ingredients):
    """Returns True if order can be made, else False for insufficient resources."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


# TODO 5: Process coins.
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins : ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# TODO 6: Check transaction successful?
def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted, else False for insufficient money"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print((f"Here's your ${change} change."))
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded!.")
        return False


# TODO 7: Make Coffee.
def make_coffee(drink_name, order_ingredient):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here's your {drink_name}☕.")


coffee_machine_mode = True
money = 0
while coffee_machine_mode:
    # TODO 1: Prompt asking user:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO 2:  Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        coffee_machine_mode = False
    # TODO 3:  Print report, when the user enters “report” to the prompt
    elif user_choice == "report":
        print(
            f"Water : {resources['water']}ml\nMilk : {resources['milk']}ml\nCoffee : {resources['coffee']}g\nMoney : ${money}")
    elif user_choice == "none":
        coffee_machine_mode = False
        print("Thank\'s for coming.")
    else:
        drink = MENU[user_choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])


