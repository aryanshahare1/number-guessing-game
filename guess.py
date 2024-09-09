import random

def number_guessing_game():
    n = random.randint(1, 100)
    guesses = 0
    a = -1
    
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    while a != n:
        try:
            a = int(input("Guess the number: "))
            guesses += 1
            
            if a > n:
                print("Lower number, please!")
            elif a < n:
                print("Higher number, please!")
        except ValueError:
            print("Please enter a valid number.")

    print(f"Congratulations! You've guessed the number {n} correctly in {guesses} attempts.")

# Run the game
number_guessing_game()