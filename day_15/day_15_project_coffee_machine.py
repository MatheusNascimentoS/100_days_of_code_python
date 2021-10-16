def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources_to_coffee(coffee):
    if resources['water'] >= MENU[coffee]['ingredients']['water']:
        if resources['coffee'] >= MENU[coffee]['ingredients']['coffee']:
            if coffee != "espresso":
                if resources['milk'] >= MENU[coffee]['ingredients']['milk']:
                    return True
                else:
                    return "milk"
        else:
            return "coffee"
    else:
        return "water"

def insert_coins():
    quarters = int(input("How many Quarters: "))
    dimes = int(input("How many Dimes: "))
    nickles = int(input("How many Nickles: "))
    pennies = int(input("How many Pennies: "))
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

def make_a_coffee(coffee):
    global money
    global resources
    resources['water'] -= MENU[coffee]['ingredients']['water']
    resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
    if coffee != "espresso":
        resources['milk'] -= MENU[coffee]['ingredients']['milk']
    money += MENU[coffee]['cost']


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

money = 0.0

while True:
    user_choice = input("What do you like? (expresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        report()
    elif user_choice == "off":
        break
    
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        enough_resources = check_resources_to_coffee(user_choice)

        if enough_resources == True:
            money_inserted = insert_coins()
            if money_inserted == MENU[user_choice]['cost']:
                make_a_coffee(user_choice)
                print(f"Here is your {user_choice} ☕ Enjoy!")
            elif money_inserted > MENU[user_choice]['cost']:
                make_a_coffee(user_choice)
                change = money_inserted - MENU[user_choice]['cost']
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {user_choice} ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry, there is not enough {enough_resources}.")
    else:
        print("Invalid input.")