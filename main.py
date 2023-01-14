from data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
money = 0

is_on = True


def make_coffee(drink_name, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name} ☕. Enjoy!")


def is_resource_sufficient(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        else:
            return True


def process_coins():
    """Takes in coins and returns the total of processed coins"""
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns true when payment is accepted or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']},\n"
              f"Milk: {resources['milk']},\n"
              f"Coffee: {resources['coffee']},\n"
              f"Money: ${money}"
              )
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])











