MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

# TODO 1.:Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer
coffee_on = True
report = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Check resources sufficient?
def resource_check(choice1, menu, resources0):
    if menu[choice1]["ingredients"]["water"] > resources0["water"]:
        print("Sorry there is not enough water")
    elif menu[choice1]["ingredients"]["milk"] > resources0["milk"]:
        print("Sorry there is not enough milk")
    elif menu[choice1]["ingredients"]["coffee"] > resources0["coffee"]:
        print("Sorry there is not enough milk")


def transaction(choice2, menu):
    money1 = menu[choice2]["cost"]
    change = value - money1
    if menu[choice2]["cost"] > value:
        print("Sorry that's not enough money. Money refunded.")
    if menu[choice2]["cost"] < value:
        report["money"] = money1
    if change > 0:
        change_rund = round(change, 2)
        print(f"your change is {change_rund}")


def deduction(choice3, menu, report0, resources1):
    water_r = resources1["water"] - menu[choice3]["ingredients"]["water"]
    milk_r = resources1["milk"] - menu[choice3]["ingredients"]["milk"]
    coffee_r = resources1["coffee"] - menu[choice3]["ingredients"]["coffee"]
    report0["water"] = water_r
    report0["milk"] = milk_r
    report0["coffee"] = coffee_r


while coffee_on:
    choice = input("What would you like? espresso/latte/cappuccino: ").lower()
    # TODO 2.:Turn off the Coffee Machine by entering “off” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    # the machine. Your code should end execution when this happens.
    # Print report.
    if choice == "off":
        break
        coffee_on = False

    if choice == "report":
        print(report)

    if choice in ["espresso", "latte", "cappuccino"]:
        print("insert your coins")
        quarters = int(input("quarters: "))
        dimes = int(input("dimes: "))
        nickels = int(input("nickels: "))
        pennies = int(input("pennies: "))
        value = float(quarters * 0.25 + dimes * 0.01 + nickels * 0.05 + pennies * 0.01)
        print(f"Here is your {choice}. Enjoy!")
        transaction(choice, MENU)
        resource_check(choice, MENU, report)
        deduction(choice, MENU, report, resources)

