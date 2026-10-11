import random

# Initialize core game values
target_number = random.randint(1, 100)
attempts = 0

print("NUMBER GUESSING GAME")
print("Guess a number between 1 and 100")

while True:
    try:
        # Prevent ValueError app crashes from empty or alphabetical inputs
        user_input = input("Enter your guess: ").strip()
        guess = int(user_input)
        
        # Prevent boundary leakage outside game rules
        if guess < 1 or guess > 100:
            print("Error: Your guess must fall between 1 and 100. Try again.")
            continue
            
    except ValueError:
        print("Error: Invalid entry. Please enter a valid whole number.")
        continue

    # Process valid turn increment
    attempts += 1
    print(f"Attempts so far: {attempts}")

    # Evaluate game loop termination metrics
    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print("Correct!")
        print(f"Success: You guessed the number in {attempts} attempts.")
        break
