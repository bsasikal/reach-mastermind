import os
from class_game import *
from prettytable import PrettyTable
from print_headers_messages import *


COMPLEXITY_DICT = {'3': 'Easy', '4': 'Normal', '5': 'Hard'}


# create a simple ASCII table for visualizing the guesses and the feedback
# using PrettyTable library
output_table = PrettyTable(['Attempts', 'Your Guess', 'Matching Digits', 'Matching Digits and Position'])

# create a simple ASCII table for printing the score table
# using PrettyTable library
score_table = PrettyTable(['Game ID', 'Complexity', 'Result', 'No.of attempts'])


# function that uses class Player and
# prints score board at the end of the game
def score_board(game):
    os.system("clear")
    print("\n###################################################")
    print("~~~~~~~~~~~~~~~~~~ MASTER MIND ~~~~~~~~~~~~~~~~~~~")
    print("###################################################\n")
    print("\t\t{}'s SCORE BOARD".format(game.name).upper())

    game_id = 0
    for idx in range(len(game.complexity)):
        game_id += 1
        score_table.add_row([game_id, COMPLEXITY_DICT[game.complexity[idx]], game.result[idx], game.num_attempt[idx]])

    print(score_table)
    print("\n\nGAME OVER!!!!!!")
    print("Nice playing {}. See you soon..!\n".format(game.name))
    input("\n\nPress Enter to continue...")
    os.system("clear")


# Function that adds details of guesses and feedback to the table
# prints the table with added details
def add_row_to_table(output_table, sno, guess, count, count_with_position):
    game_header()
    output_table.add_row([sno, guess, count, count_with_position])
    print(output_table)


def clear_table(output_table):
    output_table.clear_rows()

