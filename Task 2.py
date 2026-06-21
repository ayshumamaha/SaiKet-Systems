import random

print("===== GUESS THE NUMBER GAME =====")

while True:
    target_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target_number:
                print("Too low! Try a higher number.")

            elif guess > target_number:
                print("Too high! Try a lower number.")

            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
    
