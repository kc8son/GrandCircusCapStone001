
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
coffee_menu {
    "A": Product("Small Black Coffee", "Coffee", "Premium blended black coffee - 10 oz", 1.00),
    "B": Product("Medium Black Coffee", "Coffee", "Premium blended black coffee - 16 oz", 1.50),
    "C": Product("Large Black Coffee", "Coffee", "Premium blended black coffee - 24 oz", 2.00),
    "D": Product("Small Chai Tea", "Tea", "Oolong and black tea blend with nilk & cinnamon - 10 oz", 1.85),
    "E": Product("Medium Chai Tea", "Tea", "Oolong and black tea blend with nilk & cinnamon - 10 oz", 2.30),
    "F": Product("Large Chai Tea", "Tea", "Oolong and black tea blend with nilk & cinnamon - 10 oz", 2.90),
    "G": Product("Small Espresso", "Espresso", "Bold flavorful steam extraccted espresso - 4 oz", 1.85),
    "H": Product("Medium Espresso", "Espresso", "Bold flavorful steam extraccted espresso - 8 oz", 2.30),
    "I": Product("Large Espresso", "Espresso", "Bold flavorful steam extraccted espresso - 12 oz", 2.90),
    "J": Product("Small Mocha", "Mocha", "Our bold flavorful espresso wth chocolate & steamed milk - 8 oz", 1.85),
    "K": Product("Medium Mocha", "Mocha", "Our bold flavorful espresso wth chocolate & steamed milk - 12 oz", 2.30),
    "L": Product("Large Mocha", "Mocha", "Our bold flavorful espresso wth chocolate & steamed milk - 20 oz", 2.90)
}
customer_order = {}

####################################################################################################
#   Functions
def pos():
    print("Welcome to Cuppa Joe's Coffee Shop\nMay I take your order?")

####################################################################################################
#   Classes
class Product:
    def __init__(self, name, category, description, price):


####################################################################################################
#   Lambdas

####################################################################################################
#   Main code
if __name__ == '__main__':
    pos()