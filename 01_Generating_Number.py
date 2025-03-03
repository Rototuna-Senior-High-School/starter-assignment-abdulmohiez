# Ask the user to guess the number
import random

# List of possible numbers
correct_num_list = [i for i in range(1, 101)]  # List of numbers from 1 to 100

# Randomly select a number from the list
correct_num = random.choice(correct_num_list)

# Initialize the count variable
count = 1  # Starting count for the number of guesses

# Start the guessing loop
while count <= 10:
    guess = int(input("Please guess a number between 1 and 100: "))  # Convert input to an integer

    # Compare the guess with the randomly selected number
    if guess == correct_num:
        print("You are genius, you guessed it right.")
        break  # Exit the loop if the guess is correct
    elif guess > correct_num:
        print("Your guess is high.")
    else:
        print("Your guess is low.")
    
    count += 1  # Increment the count by 1

# If the user runs out of guesses
if guess != correct_num:
    print(f"Sorry, you've used all {count - 1} attempts. The correct number was {correct_num}.")
