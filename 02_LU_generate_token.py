import random

# Ask user for amount to spend
amount_spend = int(input("How much would you like to spend? "))

# Validate amount
if amount_spend < 1 or amount_spend > 10:
    print("Please enter an amount between $1 and $10.")
else:
    input("You are good to go. Press <Enter> to proceed.")

    # List of characters
    characters = ['Unicorn', 'Horse', 'Zebra', 'Donkey']
    # Corresponding probabilities for each character
    weights = [0.01, 0.4, 0.4, 0.19]

    # Generate tokens based on the amount spent
    generated_tokens = random.choices(characters, weights=weights, k=amount_spend)
    print("Generated Tokens:", generated_tokens)kens)
