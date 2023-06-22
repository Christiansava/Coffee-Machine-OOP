from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_off = False
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while not turn_off:
    # TODO: 1) Prompt user asking what he would like to drink.
    type_of_operation = input(f"What would you like? ({menu.get_items()}): ").lower()

    # TODO: 2) When typing "off" the machine should turn off.
    if type_of_operation == "off":
        turn_off = True
    # TODO: 3) When typing "report" we should gibe user the report with the quantities of the resources.
    elif type_of_operation == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(type_of_operation)

        # TODO: 4) After selecting the drink, check if we have sufficient resource.
        sufficient_resources = coffee_maker.is_resource_sufficient(drink)

        if sufficient_resources:
            # TODO: 5) Process customer coins.
            # TODO: 6) Check if customer coins are sufficient.
            payment_allowed = money_machine.make_payment(drink.cost)

            if payment_allowed:
                # TODO: 7) Make the coffe and reduce resource quantity.
                coffee_maker.make_coffee(drink)
