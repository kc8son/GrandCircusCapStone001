
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
#     - Future Enhancements
#     - For cash sales, validate that the amount paid is enough to cover the order
#     - Validate that the credit card number is 16 digits long
#     - Validate that the expiration date is entered in proper format
#
####################################################################################################
#   imports
import pdb
import sys
import math
import product
import payments
import validator

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

test_order = [
    ['Medium Black Coffee', 1, 1.5],
    ['Large Black Coffee', 2, 2.0],
    ['Small Chai Tea', 3, 1.85],
    ['Medium Chai Tea', 4, 2.3],
    ['Large Chai Tea', 5, 2.9]
]

####################################################################################################
#   Functions
def pos_loop():
    while True:
        total_price = 0
        customer_order = []
        pos()
        input("Press enter to start your next order. ")


def pos():
    """Main logic of the system, receives items from user, and prints receipt when it is done."""
    print("Welcome to Cuppa Joe's Coffee Shop")
    display_menu(coffee_menu)
    print("May I take your order?")
    get_status = 1
    while get_status == 1:
        get_status = get_item(coffee_menu)
    # print(customer_order)
    #process payment
    payments.Payment.payment(customer_order)
def display_menu(my_coffee_menu):
    """Displays the menu"""
    for i, (key, value) in enumerate(my_coffee_menu.items()):
        # print(i, key, value.name, value.description, value.price)
        print(f"{i}-{key} {value.name}- {value.description} \t${value.price:,.2f}")

def get_item(my_coffee_menu):
    """Receives users choice of item and allows user to quit, view menu or add items to menu"""
    choice = input("Please enter a number or letter. (quit/menu) ").upper()
    #   this indicates user is finished entering items for the order
    if choice == "QUIT":
        return 0
    #   this re displays the menu for the user
    if choice == "MENU":
        display_menu(my_coffee_menu)
        return 1
    #   this allows user to add an item
    if choice == "ADD":
        print("Enter Item Letter...")
        my_index = input("> ").upper()
        print("Enter Name...")
        my_name = input("> ")
        print("Enter Category...")
        my_cat = input("> ")
        print("Enter Description...")
        my_desc = input("> ")
        print("Enter Price...")
        my_price = float(input("> "))
        coffee_menu[my_index] = product.Product(my_name, my_cat, my_desc, my_price)
        return 1
    #   user can select menu item by number
    if choice.isdigit():
        choice = int(choice)
        if choice < 0 or choice > len(my_coffee_menu):
            print("Error: Invalid choice.")
            return 1
        #   user has selected a valid option, find out how many that user wants
        else:
            for index, (key, value) in enumerate(my_coffee_menu.items()):
                if index == choice or key == choice:
                    item = value
                    print(f"You selected: {item.name}")
                    quantity = int(input("How many would you like to order? "))
                    my_line = [item.name, quantity, item.price]
                    customer_order.append(my_line)
                    print(f"{quantity} x {item.name} = ${quantity*item.price:,.2f}")
                    #print("You ordered:", customer_order)
                    return 1
            else:
                print("Error: Invalid selection.")
                return 1
    #   this is where user selected item by letter, finds out how many of that item user wants
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


####################################################################################################
#   Classes



####################################################################################################
#   Lambdas

####################################################################################################
#   Main code
if __name__ == '__main__':
    pos_loop()
    # validator.Validator.validate_pmt("Please select the payment type: (cash/card/check)")
    # payments.Payment.payment(test_order)