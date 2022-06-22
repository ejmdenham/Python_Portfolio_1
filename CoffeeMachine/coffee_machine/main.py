# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import ResourceHandler as rh

menu = rh.menu
resources = rh.resources
c_values = rh.coin_values
refill = {"water": 300, "milk": 200, "coffee": 100, "Cash": 0}


def test(x):  # before passing in cash we get the total

    all_ingredients_present = True

    for item in menu[x]["ingredients"].items():
        if resources[item[0]] >= item[1]:
            pass
        else:
            all_ingredients_present = False
            break
    else:
        for item in menu[x]["ingredients"].items():
            if resources[item[0]] > item[1]:
                resources[item[0]] -= item[1]
        return all_ingredients_present
    return all_ingredients_present


def enough_cash(x, cash):
    cost = menu[x]["cost"]
    if cash > cost:
        print("Needed cost is", cost, "and the cash you gave was", cash)
        return True
    else:
        print("Needed cost is", cost, "and the cash you gave was", cash)
        return False


def cash_calc():
    cash = []
    cash_tot = 0
    for coin in c_values.keys():
        cash.append(int(input(f"How many {coin} would you like to insert?")))
    for i, coin_val in enumerate(c_values.values()):
        cash_tot += cash[i] * coin_val
    resources["Cash"] += cash_tot
    return cash_tot


def selection(x):
    st = test(x)
    if not st:
        return st
    else:
        cash = cash_calc()
        enough_money = enough_cash(x, cash)
        if enough_money:
            change = cash - menu[x]["cost"]
            print("Your change is:", change)
            print(f"\nAnd here's your {x}!\n")

            resources["Cash"] -= change
            return enough_money
        else:
            print("not enough")
            resources["Cash"] -= cash
            for item in menu[x]["ingredients"].items():
                resources[item[0]] += item[1]
            coffee_on()


def coffee_on():
    print("\nG'morning! How's about we getcha some coffee t'starcha day off right?")


def report():
    print("\nHere are the resource values, as requested.")
    print('______________________')
    for i in resources:
        if isinstance(resources[i], float):
            print(i, "|", round(resources[i], 2), sep="\t")
        else:
            print(i, "|", resources[i], sep="\t")
    print('----------------------')
    return True


state = True
success = True
coffee_on()
while state:
    choice = input("What can I d'ya for? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        success = selection(choice)
        if not success:
            print("sorry, refill the resources or try a different selection")
    elif "off" in choice:
        state = False
    elif "report" in choice:
        state = report()
    elif "refill" in choice:
        refill["Cash"] = round(resources["Cash"], 2)
        for val in resources:
            resources[val] = refill[val]
    else:
        print("Please choose a valid option.")
else:
    print("Okay! See ya!")
