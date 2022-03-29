from art import logo
import random

is_game_over = False
attempts = 0
CORRECT_NUMBER = random.randint(1, 100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking about a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Invalid input.")
    is_game_over = True
while not is_game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    the_guess = int(input("Make a guess: "))

    if the_guess == CORRECT_NUMBER:
        print(f"You got it! The answer was {CORRECT_NUMBER}.")
        is_game_over = True
    else:
        attempts -= 1
        if the_guess < CORRECT_NUMBER:
            print("Too Low.")
        elif the_guess > CORRECT_NUMBER:
            print("Too High.")
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer was {CORRECT_NUMBER}")
            is_game_over = True
            break
        print("Guess again.")


