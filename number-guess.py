import random
"""
Your task is to create a 'Guess the number' game in python.

You'll need to generate a random number between 1 and 100.

This number will be the 'secret' number that the user has to guess.

Set a limited number of attempts for the user to guess the number.

Use a loop to keep the game running until the user guesses the 
secret number or runs out of attempts.

Inside the loop prompt the user to enter their guess and compare 
it with the secret number.

If it is lower or higher than the secret number provide a hint to the user

If the user gets it right provide a congratulatory message and end the game.

If the user runs out of attempts provide a message telling them they
lost and reveal the secret number.
"""

secret_number = random.randint(1, 100)
attempts = 5

while attempts > 0:
    guess = int(input("Guess the secret number (between 1 and 100): "))
    if guess == secret_number:
        print("Congratulations! You guessed the secret number!")
        break
    elif guess < secret_number:
        print("The secret number is higher than your guess.")
    else:
        print("The secret number is lower than your guess.")
    attempts -= 1

if attempts == 0:
    print(f"Sorry, you lost. The secret number was {secret_number}.")
