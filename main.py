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


def ingredient_first_check(drink_name):
    for ingredient_one in MENU[drink_name]['ingredients']:
        if resources[ingredient_one] >= MENU[drink_name]['ingredients'][ingredient_one]:
            return
        else:
            print(f"Sorry..There is no enough {ingredient_one}")
            return -1

def ingredient_check(drink_name):
    for ingredient_one in MENU[drink_name]['ingredients']:
        if resources[ingredient_one] >= MENU[drink_name]['ingredients'][ingredient_one]:
            resources[ingredient_one] = resources[ingredient_one]-MENU[drink_name]['ingredients'][ingredient_one]


def calcul(drin, quard, dim, nick, penn):

    find_drink_cost = MENU[drin]["cost"]
    quard_val = (quard * 25) / 100
    dim_val = (dim * 10) / 100
    nick_val = (nick * 5) / 100
    penn_val = (penn * 1) / 100
    sum = quard_val+dim_val+nick_val+penn_val
    if sum >= find_drink_cost:
        global profit
        profit = profit+find_drink_cost
        print(f"Here is ${round(sum-find_drink_cost,2)} in change")
        print(f"Here is your {drin}☕. Enjoy!")
        return 'done'
    elif sum < find_drink_cost:
        print("Sorry that's not enough money. Money refunded")


isGame = True
while isGame:
    drink = input("What would you like? (espresso/latte/cappuccino)")
    if drink == 'off':
        isGame = False
        break
    elif drink == "report":
        water = resources['water']
        milk = resources['milk']
        coffee = resources['coffee']
        money = profit
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee:{coffee}g\nMoney:${money}")
        continue
    # print(ingredient_check(drink))
    if ingredient_first_check(drink) == -1:
        continue
    print("Please insert coins.")
    quarters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickels = int(input("how many nickels?"))
    penny = int(input("how many pennies?"))
    if(calcul(drink, quarters, dimes, nickels, penny)) == 'done':
        ingredient_check(drink)


