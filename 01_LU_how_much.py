#ask user how much would he like to spend must be greater and equla to 1$ and less than or equal to 10$
amount_spend = int(input("How much would you like to spend? "))
if amount_spend <= 0 or amount_spend > 10 :
 print("Please enter amount of money you are willing to spend between 1$ and 10$")
else:
 print("You are good to go press <enter> to proceed.")
