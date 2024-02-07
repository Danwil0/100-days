from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

espresso_men = MenuItem("espresso", "50", "0", "18", "1.5")
latte_men = MenuItem("latte", "200", "150", "24", "2.4")
cappa_men = MenuItem("cappuccino", "250", "100", "24", "3.5")


while is_on:
    order_name = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order_name == "off":
        is_on = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)









