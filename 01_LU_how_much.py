import random

# Ask user for amount to spend
amount_spend = int(input("How much would you like to spend? "))

# Validate amount
if amount_spend < 1 or amount_spend > 10:
    print("Please enter an amount between $1 and $10.")
else:
    input("You are good to go. Press <Enter> to proceed.")
