import random

choices = ["stone", "paper", "scissors"]

print("Welcome to Stone, Paper, Scissors!")
print("Enter your choice: stone, paper, or scissors")
print("Type 'exit' to end the game.")

while True:
    user_choice = input("Your choice: ").lower()
    if user_choice == 'exit':
        break

    if user_choice not in choices:
        print("Invalid choice! Please enter stone, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

print("Thank you for playing!")
