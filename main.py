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
    "water": {
        "value": 200,
        "unit": "ml"
    },
    "milk": {
        "value": 200,
        "unit": "ml"
    },
    "coffee": {
        "value": 100,
        "unit": "g"
    },
    "money": {
        "value": 0,
        "unit": "$"
    }
}


def welcome() -> None:
    drinks = []
    active = True
    for itm in MENU.keys():
        drinks.append(itm)
    while active:
        choice = input(f"What would you like? ({drinks[0]}/{drinks[1]}/{drinks[2]}):")
        if choice == "off":
            active = False
            print("Thank you, goodbye for now!")
        if choice == "report":
            print_report()
        if choice in ["espresso", "latte", "cappuccino"]:
            enough_resources = check_resources(choice)
            if enough_resources:
                enough_money = check_money(choice)
                if enough_money:
                    make_coffee(choice)


def round_numbers(num) -> int:
    return round(num, 2)


def get_drink(choice) -> dict:
    return MENU[choice]


def print_report() -> None:
    for rsc in resources:
        value = resources[rsc]["value"]
        unit = resources[rsc]["unit"]
        print(f"{rsc.capitalize()}: {value}{unit}")
    print("")


def check_resources(choice) -> bool:
    drink = get_drink(choice)
    ingredients = drink["ingredients"]
    # check resource levels
    makeable = True
    for ing in ingredients:
        print(f"Checking {ing} level...")
        if resources[ing]["value"] < ingredients[ing]:
            print(f"Sorry, there is not enough {ing}")
            makeable = False
            break
        else:
            print(f"Enough {ing} for {choice}")
            print("")
    return makeable


def check_money(choice) -> bool:
    drink = get_drink(choice)
    money_added = 0
    cost = drink["cost"]
    makeable = False
    print(f"Total amount: ${cost}")
    print("Insert coins")
    coins = [
        {
            "name": "quarters",
            "value": 0.25
        },
        {
            "name": "dimes",
            "value": 0.10
        },
        {
            "name": "nickels",
            "value": 0.05
        },
        {
            "name": "pennies",
            "value": 0.01
        }
    ]
    for i in range(len(coins)):
        coin_name = coins[i]["name"]
        coins_input = input(f"{coin_name.capitalize()}: ")
        coins[i]["number"] = coins_input
        money_added += round_numbers((int(coins_input) * coins[i]["value"]))
    if money_added >= cost:
        print("")
        print(f"Added ${money_added}")
        print("")
        print(f"One {choice} coming right up!")
        resources["money"]["value"] += cost
        change = round_numbers(money_added - cost)
        if change > 0:
            print(f"Here is ${change} in change")
            makeable = True
    else:
        print(f"Sorry ${money_added} is not enough money. Money refunded.")
    return makeable


def make_coffee(choice):
    drink = get_drink(choice)
    ingredients = drink["ingredients"]
    for ing in ingredients:
        resources[ing]["value"] -= ingredients[ing]
    print("")
    print_report()
    

welcome()