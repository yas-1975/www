import random

player_score = 0
computer_score = 0

continue_game = "y"

while continue_game != "n":

    player_choice = str(input("Please enter Rock(r), Paper(p), or Scissors(s):"))
    computer_choice = ["Rock", "Paper", "Scissors"]
    computer_option = random.choice(computer_choice)

    if player_choice == "r":
        player_choice = "Rock"
    elif player_choice == "p":
        player_choice = "Paper"
    elif player_choice == "s":
        player_choice = "Scissors"
    else:
        print(player_choice, " is an invalid chose")

    print("You chose:", player_choice, "Computer chose:", computer_option)

    if player_choice == computer_option:
        print("Game was a tie")

    elif player_choice == "Rock":
        if computer_option == "Paper":
            print("Paper covers Rock, you lose")
            computer_score += 1
        else:
            print("Rock breaks Scissors, You Win")
            player_score += 1
    elif player_choice == "Paper":
        if computer_option == "Scissors":
            print("Scissors cuts Paper, you lose")
            computer_score += 1
        else:
            print("Paper covers Rock, You Win")
            player_score += 1

    elif player_choice == "Scissors":
        if computer_option == "Rock":
            print("Rock Breaks Scissors, you lose")
            computer_score += 1
        else:
            print("Scissors cuts Paper, You Win")
            player_score += 1

    continue_game = input("Play Again (y/n)")

print("Player Score:", player_score)
print("Computer Score:", computer_score)
if player_score == computer_score:
    print("Game is a draw")
if player_score > computer_score:
    print("You win!!!")
if player_score < computer_score:
    print("Computer Win, You Lose!!!!")
