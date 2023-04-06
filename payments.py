####################################################################################################
#
#   Date Written: 03/30/2023        By: Joseph P. Merten & Romana Choudhury
#   payment object
#
####################################################################################################
#   imports
import validator

cup = """
   ~
   ~
 .---.
 `---'=.
 | Joe| |
 |    |='
 `---'"""

####################################################################################################
#   Classes
class Payment():
    def payment(my_order_list):
        """This METHOD will calculate extended prices (qty * price) and sales tax.."""
        new_list = []
        sub_total = 0
        for line in my_order_list:
            extended_price = line[1] * line[2]
            new_list.append([line[0], line[1], line[2], extended_price])
            sub_total += extended_price
        print(f"Subtotal for your order: ${sub_total:,.2f}")
        sales_tax = sub_total * .07
        print(f"Sales tax for your order: ${sales_tax:,.2f}")
        grand_total = sub_total + sales_tax
        pmt_type = validator.Validator.validate_pmt("Please select the payment type: (cash/card/check)")
        if pmt_type == "cash":
            cash_pmt(grand_total)
        elif pmt_type == "check":
            check_pmt(grand_total)
        elif pmt_type == "card":
            card_pmt(grand_total)
        else:
            print("something went wrong...")
        print("")
        for line in new_list:
            print(f"{line[1]} x {line[0]} at ${line[2]:,.2f} = ${line[3]:,.2f}")

    def get_payment_type(self):
        """This method will ask what the method of payment will be..."""


def card_pmt(my_charge):
    """This function will process a credit card payment."""
    print("Please enter the card number:")
    my_card_no = input("> ")
    print("Please enter the card expiration date:")
    my_card_date = input("> ")
    print("Please enter the card CVV:")
    my_card_cvv = input("> ")
    print(f"\n\n\n\n\n{cup}\nThank you for paying  ${my_charge:,.2f} with card number: {my_card_no}")


def cash_pmt(my_charge):
    """This method will process a cash payment.  All we need to do is ask for the amount of
    money tendered and compute change."""
    print("Please enter the amount tendered:")
    cash_amt = float(input("> "))
    # cash_amt = validator.Validator.validate_cash("Please enter the amount tendered:", my_charge)
    change = cash_amt - my_charge
    print(f"\n\n\n\n\n{cup}\nThank you for paying  ${cash_amt:,.2f} for your purchase of ${my_charge:,.2f}, you get ${change:,.2f} in change")



def check_pmt(my_charge):
    """This method will proceess a check payment.  All we need to do here is ask for the check number."""
    print("Please enter the check number:")
    my_check_no = input("> ")
    print(f"\n\n\n\n\n{cup}\nThank you for paying ${my_charge:,.2f} with check number: {my_check_no}")