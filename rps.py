import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player} whereas Computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "paper":
            return "You lose"
        else:
            return "You win......"
    elif player == "paper":
        if computer == "rock":
            return "You win!!"
        else:
            return "you lose!"
    elif player == "scissors":
        if computer == "paper":
            return "You win!"
        else:
            return "You lose"

choices = get_choices()
outcome = check_win(choices["player"], choices["computer"])
print(outcome)