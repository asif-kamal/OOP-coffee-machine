from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True
money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

while machine_is_on:
    choice = input("What drink would you like? Type 'espresso' or 'latte' or 'cappuccino': ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_is_on = False
    else:
        found_menu_item = menu.find_drink(choice)
        money_machine.make_payment(found_menu_item.cost)

        if coffee_maker.is_resource_sufficient(found_menu_item):
            coffee_maker.make_coffee(found_menu_item)




