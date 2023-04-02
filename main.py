
####################################################################################################
#
#   Date Written: 03/27/2023        By: Joseph P. Merten & Romana Choudhury
#   Capstone Project 001:
#   Project URL: https://docs.google.com/document/d/1jlyrQUdswsKmK4deeztNaCFhjF1gyPDF/preview
#
#   POS Terminal for Cuppa Joe Coffee Shop...
#   - Build a menu of coffee items. (dictionary)
#   - Create Payment class
#     - Create CashPayment
#     - Create CreditCardPayment
#     - Create CheckPayment
#
####################################################################################################
#   imports
import pdb
import sys
import math
import product

####################################################################################################
#   Variables
coffee_menu = {
    "A": product.Product("Small Black Coffee", "Coffee", "Premium blended black coffee - 10 oz", 1.00),
    "B": product.Product("Medium Black Coffee", "Coffee", "Premium blended black coffee - 16 oz", 1.50),
    "C": product.Product("Large Black Coffee", "Coffee", "Premium blended black coffee - 24 oz", 2.00),
    "D": product.Product("Small Chai Tea", "Tea", "Oolong and black tea blend with milk & cinnamon - 10 oz", 1.85),
    "E": product.Product("Medium Chai Tea", "Tea", "Oolong and black tea blend with milk & cinnamon - 10 oz", 2.30),
    "F": product.Product("Large Chai Tea", "Tea", "Oolong and black tea blend with milk & cinnamon - 10 oz", 2.90),
    "G": product.Product("Small Espresso", "Espresso", "Bold flavorful steam extracted espresso - 4 oz", 1.85),
    "H": product.Product("Medium Espresso", "Espresso", "Bold flavorful steam extracted espresso - 8 oz", 2.30),
    "I": product.Product("Large Espresso", "Espresso", "Bold flavorful steam extracted espresso - 12 oz", 2.90),
    "J": product.Product("Small Mocha", "Mocha", "Our bold flavorful espresso wth chocolate & steamed milk - 8 oz", 1.85),
    "K": product.Product("Medium Mocha", "Mocha", "Our bold flavorful espresso wth chocolate & steamed milk - 12 oz", 2.30),
    "L": product.Product("Large Mocha", "Mocha", "Our bold flavorful espresso wth chocolate & steamed milk - 20 oz", 2.90)
}
customer_order = []
total_price = 0
####################################################################################################
#   Functions
def pos():
    print("Welcome to Cuppa Joe's Coffee Shop")
    display_menu(coffee_menu)
    print("May I take your order?")
    get_status = 1
    while get_status == 1:
        get_status = get_item(coffee_menu)
    print(customer_order)
    #process payment
def display_menu(my_coffee_menu):
    for i, (key, value) in enumerate(my_coffee_menu.items()):
        # print(i, key, value.name, value.description, value.price)
        print(f"{i}-{key} {value.name}- {value.description} \t${value.price:,.2f}")
def get_item(my_coffee_menu):
    choice = input("Please enter a number or letter. (quit/menu) ").upper()
    if choice == "QUIT":
        return 0
    if choice == "MENU":
        display_menu(my_coffee_menu)
        return 1
    if choice.isdigit():
        choice = int(choice)
        if choice < 0 or choice > 11:
            print("Error: Invalid choice.")
            return 1
        else:
            for index, (key, value) in enumerate(my_coffee_menu.items()):
                if index == choice or key == choice:
                    item = value
                    print(f"You selected: {item.name}")
                    quantity = int(input("How many would you like to order? "))
                    my_line = [item.name, quantity, item.price]
                    customer_order.append(my_line)
                    #print("You ordered:", customer_order)
                    return 1
            else:
                print("Error: Invalid selection.")
                return 1
    elif choice.isalpha():
        if choice in my_coffee_menu:
            item = my_coffee_menu[choice]
            print(f"You selected: {item.name}")
            quantity = int(input("How many would you like to order? "))
            my_line = [item.name, quantity, item.price]
            customer_order.append(my_line)
            #print("You ordered:", customer_order)
            return 1
        else:
            print("Error: Invalid input.")
            return 1
    else:
        print("Error: Invalid input.")
        return 1

    # response = input("Would you like to continue shopping? y/n ")
    # if response.lower() == "y":




    #     convert choice to integer
    #     if choice is too big or too small:
    #         error message to try again
    # if choice is not in dictionary
    #     error message to try again
    # else:
    #     error message to try again
    # ask for quantity
    # add choice to customer_order

####################################################################################################
#   Classes



####################################################################################################
#   Lambdas

####################################################################################################
#   Main code
if __name__ == '__main__':
    pos()