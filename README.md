# **_GrandCircusCapStone001 - Romana & Joe's project_**
First capstone project

Cuppa Joe Coffee shop

Written in python for Cuppa Joe

Files used:
1. main.py - This is the main POS system for Cuppa Joe 
   1. Functionality includes
      1. ordering an item from the menu using a number or a letter
      4. redisplaying the menu - menu
      5. adding items to the menu (hidden) - add 
2. products.py
   1. This file simply defines our product object with the following properties: name, category, description, price
3. payments.py
   1. provides user with total cost of items selected
   2. asks for payment type 
   3. displays receipt after selecting payment type
4. validator.py
    1. This file contains validator object which performs various validation.
       1. validating payment type
       

**Future enhancements:**
- For cash sales, validate that the amount paid is enough to cover the order
- Validate that the credit card number is 16 digits long
- Validate that the credit card expiration date is entered in proper format