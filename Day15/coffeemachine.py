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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(ordered_items):
    for item in ordered_items:
        if ordered_items[item] >= resources[item]:
            print("Sorry there is not enough {item}.")
            return False
        else:
            return True


def check_amount(drink_cost, profit):
    quarter = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickel = int(input("Enter the number of nickel: "))
    pennies = int(input("Enter the number of pennies: "))
    total_amount = (0.25*quarter)+(0.10*dimes)+(0.05*nickel)+(0.01*pennies)
    if total_amount >= drink_cost:
        profit += drink_cost
        amount_returned = round(total_amount - drink_cost, 2)
        print(f"Here's your change ${amount_returned}.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


enough_resources = True


while enough_resources:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        enough_resources = False
    elif choice == "report":
        print("Water: {}ml\nMilk: {}ml\nCoffee: {}g\nMoney: ${}".format(resources["water"],resources["milk"],resources["coffee"], amount_generated))
    else:
        result = check_resources(MENU[choice]["ingredients"])
        if result:
            print("There are enough resources to make the drink.")
            print("Please insert the amount of coins required to purchase the drink. The price of the drinks are:\nEspresso: ${},\nLatte: ${},\nCappuccino: ${}".format(MENU["espresso"]["cost"], MENU["latte"]["cost"], MENU["cappuccino"]["cost"]))
            if check_amount(MENU[choice]["cost"], profit):
                make_coffee(choice, MENU[choice]["ingredients"])
        else:
            enough_resources = False