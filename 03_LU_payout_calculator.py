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
    print("Generated Tokens:", generated_tokens)

    # Calculate winnings
    total_winnings = 0

    for token in generated_tokens:
        if token in ['Zebra', 'Horse']:
            amount_won = 0.5
            amount_spend -= 0.5  # Deduct $0.50
        elif token == 'Unicorn':
            amount_won = 5
            amount_spend += 5  # Add $5
        else:  # Donkey case
            amount_won = 0
            amount_spend -= 1  # Deduct $1
        
        total_winnings += amount_won
        if amount_won > 0:
            print(f"Congratulations! You won ${amount_won:.2f}")
        else:
            print("Sorry, you did not win anything this round.")

    # Display final balance
    print(f"Your final balance is: ${amount_spend:.2f}")

    # Simulate payment check
    confirm_payment = input("Confirm payment of ${:.2f} (yes/no): ".format(amount_spend)).strip().lower()

    if confirm_payment == "yes":
        print("Payment successful! Enjoy your tokens.")
    else:
        print("Payment canceled. No tokens generated.")

