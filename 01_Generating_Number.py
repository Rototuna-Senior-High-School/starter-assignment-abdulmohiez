import random

user_wish = 'yes'

while user_wish.lower() == 'yes':
    # List of possible numbers
    correct_num_list = [i for i in range(1, 101)]  # List of numbers from 1 to 100

    # Randomly select a number from the list
    correct_num = random.choice(correct_num_list)

    # Initialize the count variable
    count = 1  # Starting count for the number of guesses
    guessed_numbers = []  # List to store the numbers already guessed

    # Start the guessing loop
    while count <= 10:
        guess = int(input("Please guess a number between 1 and 100: "))  # Convert input to an integer

        # Check if the number has already been guessed
        if guess in guessed_numbers:
            print("You've already guessed that number. Try again.")
            continue  # Skip the rest of the loop and ask for another guess

        # Add the guess to the guessed_numbers list
        guessed_numbers.append(guess)

        # Compare the guess with the randomly selected number
        if guess == correct_num:
            print("You are genius, you guessed it right.")
            break  # Exit the loop if the guess is correct
        elif guess > correct_num:
            print("Your guess is high.")
        else:
            print("Your guess is low.")
        
        count += 1  # Increment the count by 1 for each unique guess

    # If the user runs out of guesses
    if guess != correct_num:
        print(f"Sorry, you've used all {count - 1} attempts. The correct number was {correct_num}.")
  
    user_wish = input("Do you want to play another round? (yes/no) ")
