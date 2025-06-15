import random

amount_spend = int(input("Please enter the amount that you want to spend." ))

if amount_spend < 0 or amount_spend > 10:
 print("Please enter the amount between 0 and 10$.")

list_of_characters = ["Unicorn", "Horse","Zebra","Donkey"]
weights = [0.01, 0.4, 0.4, 0.19]

generated_token = random.choices(list_of_characters ,weights=weights, k=amount_spend)
print("Generated Tokens:", generated_token)

amount_earned = 0
total_winning = 0
for token in generated_token:
  if token in ['Zebra','Horse']:
    amount_earned += 0.5
    amount_spend -= 0.5
  
  elif token == "Unicorn":
    amount_earned += 10
    amount_spend += 10
  
  else: token == "Donkey"
  amount_earned += 0
  amount_spend -= 1
  
  
if amount_earned > 0:
  print("Congratulations, You made profit!")
else:
  print("Sorry, You made lost")
    
print("You earned", amount_earned)
