MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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

def coin_handler():
    print("Please insert coins.")
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    money_inserted = quarters * 0.25 + dimes *0.1 + nickles *0.05 + pennies *0.01
    return money_inserted

def change_calculator(MENU,money,drink):
   drink_cost = float(MENU[drink]['cost'])
   change = money - drink_cost
   return change

def give_change_or_refuse_transaction(change,human_request):
    if change >= 0:
        print(f"Here is your ${change} change!\nHere is your {human_request}. Enjoy!")
        successful_transaction = True
    else:
        print("Sorry that's not enough money. Money refunded!")
        successful_transaction = False
    return successful_transaction

def resources_checker(MENU,machine_resources,human_request):
    ingredients = list(MENU['latte']['ingredients'])
    ingredient_is_available = {}
    for item in ingredients:
        if machine_resources[item] - MENU[human_request]['ingredients'][item] > 0:
            ingredient_is_available[item] = 1
        else:
            ingredient_is_available[item] = 0
    return ingredient_is_available

machine_resources = resources
machine_resources['Money'] = 0.0

machine_is_on = True

while machine_is_on == True:

    human_request = input("What would you like? (espresso/latte/cappuccino):")

    if human_request == 'report':
        for item in machine_resources:
            print(f"{item:6} :{machine_resources[item]}")
    
    elif human_request == 'off':
        machine_is_on = False
    
    elif human_request in ['espresso','latte','cappuccino']:
        ingredient_is_available = resources_checker(MENU,machine_resources,human_request)
        if  sum(ingredient_is_available.values()) == 3:
            money = coin_handler()
            change = change_calculator(MENU,money,human_request)
            successful_transaction = give_change_or_refuse_transaction(change,human_request)
            if successful_transaction == True:
                machine_resources['water'] -= MENU[human_request]['ingredients']['water']
                machine_resources['milk'] -= MENU[human_request]['ingredients']['milk']
                machine_resources['coffee'] -= MENU[human_request]['ingredients']['coffee']
                machine_resources['Money'] += MENU[human_request]['cost']
        else:
          ingredients_not_available = []
          for item in ingredient_is_available:
            if ingredient_is_available[item] == 0:
                ingredients_not_available.append(item)
          print('Sorry there is not enough', ingredients_not_available)

        
  

# TODO update resources


    


