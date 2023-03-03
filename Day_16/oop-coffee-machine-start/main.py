from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on :
  options = menu.get_items()
  choice = input(f"What would you like to drink? ({options})")

  if choice == 'off':
    is_on = False
  elif choice == 'report':
    coffe_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if  coffe_maker.is_resource_sufficient(drink):
      cost = drink.cost
      if money_machine.make_payment(cost):
        coffe_maker.make_coffee(drink)
    



  


