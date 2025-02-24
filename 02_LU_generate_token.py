#ask user how much would he like to spend must be greater and equla to 1$ and less than or equal to 10$

amount_spend = int(input("How much would you like to spend? "))

if amount_spend <= 0 or amount_spend > 10 :
 print("Please enter amount of money you are willing to spend between 1$ and 10$")
else:
 input("You are good to go. Press <Enter> to proceed.")

 
import random

# List of characters
characters = ['Unicorn', 'Horse', 'Zebra', 'Donkey']

# List of corresponding weights (probabilities) for each character
weights = [0.01, 0.4, 0.4, 0.19]  # The sum of weights should ideally be 1, but it's not mandatory

# Define the number of tokens to generate
num_tokens = amount_spend

# Randomly select 'num_tokens' tokens from the list
generated_tokens = random.choices(characters, k=num_tokens)

print("Generated Tokens:", generated_tokens)