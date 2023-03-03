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

def resources_checker(MENU,machine_resources,human_request):
    ingredients = list(MENU['latte']['ingredients'])
    ingredient_is_available = {}
    for item in ingredients:
        if machine_resources[item] - MENU[human_request]['ingredients'][item] > 0:
            ingredient_is_available[item] = 1
        else:
            ingredient_is_available[item] = 0
    return ingredient_is_available

dict = resources_checker(MENU,resources,'latte')
print(sum(dict.values()))
     