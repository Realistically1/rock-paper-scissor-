import random

def get_player_choice():
    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice in ['rock', 'paper', 'scissors']:
            return player_choice
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

def main():
    player_score = 0
    computer_score = 0
    rounds_to_win = 2

    print("Welcome to Rock, Paper, Scissors!")

    while player_score < rounds_to_win and computer_score < rounds_to_win:
        print("\nRound start!")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose {player_choice}. The computer chose {computer_choice}.")

        winner = determine_winner(player_choice, computer_choice)

        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'player':
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score - Player: {player_score}, Computer: {computer_score}")

    if player_score > computer_score:
        print("\nCongratulations! You win the game!")
    else:
        print("\nComputer wins the game. Better luck next time!")

if __name__ == "__main__":
    main()
