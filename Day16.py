# Coffee Machine Project using OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_obj = CoffeeMaker()
menu_obj = Menu()
money_machine_obj = MoneyMachine()

coffee_machine_on = True

while coffee_machine_on:
    options = menu_obj.get_items()
    choice = input(f"What would you like? ({options}) : ")
    if choice == "off":
        coffee_machine_mode = False
    elif choice == "report":
        # TODO 1: Print report
        coffee_maker_obj.report()
        money_machine_obj.report()
    else:
        drink = menu_obj.find_drink(choice)
        # TODO 2: Check resources sufficient?
        if coffee_maker_obj.is_resource_sufficient(drink):
            # TODO 3: Process coins
            # TODO 4: Check transaction successful?
            if money_machine_obj.make_payment(drink.cost):
                # TODO 5: Make coffee
                coffee_maker_obj.make_coffee(drink)
