
import random

print("NUMBER GUESSING GAME")

while True:
    target_number = random.randint(1, 100)
    attempts = 0

    print("\nGuess a number between 1 and 100")

    while True:
        try:
            user_input = input("Enter your guess: ").strip()
            guess = int(user_input)

            if guess < 1 or guess > 100:
                print("Error: Guess must be between 1 and 100.")
                continue

        except ValueError:
            print("Error: Enter a valid whole number.")
            continue

        attempts += 1
        print(f"Attempts so far: {attempts}")

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print("Correct!")
            print(f"You guessed the number in {attempts} attempts.")
            break

    # Play Again feature
    play_again = input(
        "Do you want to play again? (yes/no): "
    ).strip().lower()

    if play_again not in ("yes", "y"):
        print("Thanks for playing!")
        break
        
