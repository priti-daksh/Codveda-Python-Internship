import random
secret_number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")
attempts = 0
max_attempts = 7

while attempts < max_attempts:
    print("\nAttempt", attempts + 1)

    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue 

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number! 🎉")
        break
if attempts == max_attempts:
    print("\nGame Over!")
    print("The correct number was:", secret_number)
