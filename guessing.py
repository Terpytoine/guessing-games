import random

def number_guessing_game():
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100.")
    print("Can you guess what it is?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess > number:
                print("Too high! Try again.")
            elif guess < number:
                print("Too low! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()
