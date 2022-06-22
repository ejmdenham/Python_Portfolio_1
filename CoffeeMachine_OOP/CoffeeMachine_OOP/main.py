from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu, coffee, mm = Menu(), CoffeeMaker(), MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What can I d'ya for? ({options}...): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report(), mm.report()
    elif choice == "refill":
        coffee.refill()
    elif menu.find_drink(choice):
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
            coffee.make_coffee(drink)  # makes coffee and deducts resources
else:
    print("Okay! See ya!")
