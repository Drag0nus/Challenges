from random import *

# print("Let's play!")
# choices = {
#     1: "rock",
#     2: "paper",
#     3: "scissors"
# }
#
# user_AI = choices[randint(1, 3)]
# print(user_AI)


def rock_paper_scissors():
    first_user_move = input("First player's move: ").lower()
    second_user_move = input("Second player's move: ").lower()

    if first_user_move == "rock" and second_user_move == "scissors" or \
                            first_user_move == "scissors" and second_user_move == "paper" or \
                            first_user_move == "paper" and second_user_move == "rock":
        print("First user wins. Flawless victory")
    elif second_user_move == "rock" and first_user_move == "scissors" or \
                            second_user_move == "scissors" and first_user_move == "paper" or \
                            second_user_move == "paper" and first_user_move == "rock":
        print("Second user wins. Flawless victory")
    elif first_user_move == second_user_move:
        print("It's a draw.")
    else:
        print("You entered wrong value. Try again.")
        rock_paper_scissors()

    new_game = input("Do you want start new game? y/n: ")
    while new_game == "y":
        rock_paper_scissors()
        if new_game == "n":
            print("Ok. Have a nice day!")
            break


rock_paper_scissors()
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
#
# Remember the rules:
#
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock
