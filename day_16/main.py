from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True


while is_on:
    user_choice = input(f"What do you like? ({menu.get_items()}) ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            

