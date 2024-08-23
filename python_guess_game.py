import random

name: str = input("Enter your name: ")
score: int = 0

while True:
    random_number: int = random.randint(1, 100)
    print(f"\nMr. {name}, your random number is = {random_number}")

    computer_number: int = random.randint(1, 100)
    print("Computer has generated a random number....")
    print("Guess if the computer's random number is higher than your generated number or lower?")
    guess: str = input("Higher or Lower (or type 'exit' to end the game): ")

    if guess.lower() == "higher":
        if computer_number > random_number:
            score += 1
            print(f"You won! Your score is {score}")
            print(f"Computer's number was {computer_number}")
        else:
            print(f"Wrong guess. The computer's number was {computer_number}")
    elif guess.lower() == "lower":
        if computer_number < random_number:
            score += 1
            print(f"You won! Your score is {score}")
            print(f"Computer's number was {computer_number}")
        else:
            print(f"Wrong guess. The computer's number was {computer_number}")
    elif guess.lower() == "exit":
        print("Game over.")
        print(f"Final score: {score}")
        break
    else:
        print(f"Invalid input. The computer's number was {computer_number}")

print("Thank you for playing!")
