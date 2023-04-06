####################################################################################################
#
#   Date Written: 04/03/2023        By: Joseph P. Merten
#   Various validation methods
#
####################################################################################################
#   imports

####################################################################################################
#   Classes
class Validator():
    def validate_yn(my_prompt):
        "This METHOD validates a yes/no response."
        my_resp = 'x'
        while my_resp != 'n' and my_resp != 'y':
            my_resp = input(my_prompt).lower()
            if my_resp != 'n' and my_resp != 'y':
                print("Invalid response, please enter 'y' or 'n'...")
        return my_resp


    def validate_pmt(my_prompt):
        "This METHOD validates a payment method of cash/card/check."
        my_resp = 'x'
        while my_resp not in "cash card check":
            print(my_prompt)
            my_resp = input("> ").lower()
            if my_resp not in "cash card check":
                print("Invalid response, please enter cash/card/check...")
        return my_resp
    def validate_int(my_prompt, min, max):
        """This method will display a message and validate that the response is an
        integer within the boundaries specified by min & max"""
        my_resp = min - 5   #force untrue...
        while not min <= my_resp <= max:
            print(my_prompt)
            my_resp = input()
            try:
                my_resp = int(my_resp)
            except:
                my_resp = min - 5
            if not min <= my_resp <= max:
                print("Invalid entry, please try again...")
        return my_resp


    def validate_cash(my_prompt, amount_due):
        """This method validates the amount the user will be paying, it has to be greater than or equal to amount that is due"""
        my_resp = amount_due - 5.0
        while my_resp < amount_due:
            print(amount_due)
            my_resp = input(my_prompt)
            try:
                my_resp = float(my_resp)
            except:
                my_resp = amount_due - 5.0
            if my_resp < amount_due:
                print("Invalid entry, please try again...")
        return my_resp
