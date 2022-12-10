#!/usr/bin/python3

available_pizzas = ['Small Pizza', 'Medium Pizza', 'Large Pizza']
available_toppings = ['Pepperoni for Small Pizza', 'Pepperoni for Medium Pizza', 'Pepperoni for Large Pizza','Extra Cheese']
pizza_prices = {'Small Pizza':15, 'Medium Pizza':20, 'Large Pizza':25}
topping_prices = {'Pepperoni for Small Pizza':2, 'Pepperoni for Medium Pizza': 3, 'Pepperoni for Large Pizza':3, 'Extra Cheese':1}
sub_total = []
final_order = {}

#ordering a pizza
print("Hi, welcome to our text based pizza ordering")
order_pizza = True
while order_pizza:    
    print("Please choose a pizza: ")
    print()
    for pizzas in available_pizzas:
        print(pizzas)
        print()
    while True:
        pizza = input("which pizza would you like to order?")
        if pizza in available_pizzas:
            print(f"You have ordered a {pizza}.")
            sub_total.append(pizza_prices[pizza])
            break
        if pizza not in available_pizzas:
            print(f" am sorry, we currently do not have {pizza}.")

    #asking for extra toppings
    order_topping = True
    print("This is the list of available extra toppings: ")
    for toppings in available_toppings:
        print(toppings)
        print()
    while order_topping:
        extra_topping = input("Would you like an extra topping? yes or no?")
        if extra_topping == "yes":
            topping = input("Which one would you like to add?")
            if topping in available_toppings:
                final_order.setdefault(pizza, [])
                final_order[pizza].append(topping)
                print(f"he added {topping}.")
                sub_total.append(topping_prices[topping])
            else:
                print(f"iam sorry, we don't have {topping} available.")

        elif extra_topping == "no":
            break
    extra_pizza = input("Would you like to order another pizza?")
    if extra_pizza == "no":
        for key, value in final_order.items():
            print(f"\nYourorder a {key} pizza with {value}")
        check_order = True
        while check_order:
            print()
            order_correct = input("Is this correct? yes/no ")
            if order_correct == "yes":
                check_order = False
                order_pizza = False
            if order_correct == "no":
                print(final_order)
                add_remove = input("would you like to add or remove? ")
                if add_remove == "remove":
                    remove = input("Which pizza would you like to remove? ")
                    del final_order[remove]
                    print(final_order)
                if add_remove == "add":
                    check_order = False

#finalizing the order
print(f"\nYour total order price is: ${sum(sub_total)}")
