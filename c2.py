#Rock Paper Scissors Game

import random

def get_user_choice():
    user_input = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    while user_input not in ['rock', 'paper', 'scissors', 'quit']:
        user_input = input("Invalid choice. Please enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    return user_input

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':
            print("Gamer Over!")
            break
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    play_game()