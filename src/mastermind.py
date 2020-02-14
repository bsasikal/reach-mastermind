import os
import copy
from colorama import Fore

from score_board import *
from class_game import *
from print_headers_messages import *
from api_random_number_generation import *
from helper_functions import *

NO_OF_ATTEMPTS = 10


# Function that has the core game logic
# get both random number and player's guess
# calculate count and count_with_position
# print guess and feedback to the table
def main_logic():
    # player chooses the level of complexity in the game.
    complexity = choose_game_complexity()

    # generates random number; returns a list
    random_num_list = generate_random_number(complexity)
    random_num_len = len(random_num_list)

    # get the player's guess; returns a string of digits
    guess = guess_the_number(random_num_len)
    # convert the guessed number into a list
    guess_list = list(map(int, guess))

    # check if the player's guess and random number are equal
    if guess_list == random_num_list:
        print("Great! You guessed the number in just 1 try!\n")
        game.append_player_data(complexity, 'Success', 1)
        success_message(1)
    else:
        # attempt variable initialized.
        # It will keep count of the number of tries the player takes to guess the number.
        attempt = 0

        # Loop for 10 attempts
        while attempt < NO_OF_ATTEMPTS:
            # increment the variable attempt
            attempt += 1

            # call the helper function that calculates count and count_with_position
            count, count_with_position = calculate_count_and_count_with_position(random_num_list, guess_list)

            add_row_to_table(output_table, attempt, guess, count, count_with_position)

            # if the player guessed the right number
            if count == count_with_position and guess_list == random_num_list:
                # for score board
                game.append_player_data(complexity, 'Success', attempt)
                success_message(attempt)
                break

            # if the player maxed out 10 attempts
            if attempt == NO_OF_ATTEMPTS:
                # for score board
                game.append_player_data(complexity, 'Failed', attempt)
                sorry_message(random_num_list)
                break

            if 7 <= attempt < 9:
                print(Fore.RED + "\nWARNING: You now have only {} attempt(s) left to guess the number.... ".format(
                    10 - attempt) + Fore.RESET)
            elif attempt == 9:
                print(Fore.RED + "\nWARNING: Your FINAL chance to guess the number.... " + Fore.RESET)

            # guess the number again
            guess = guess_the_number(random_num_len)
            guess_list = list(map(int, guess))


# Main function
if __name__ == '__main__':
    # Create an object for class Game
    game = Game()

    os.system("clear")

    # call helper function to accept & validate player's name as input
    name = get_input_name()
    game.name = name.capitalize()

    os.system("clear")
    print("\nHello {}.. Welcome to the game!".format(game.name))

    # call function game_header to print game header and rules
    game_header()

    # call helper function that decides if user wants to play game or not
    play_game = play_or_play_again(False)

    # only if the player wants to play
    while play_game == 'Y':
        # Calls the function play by passing boolean 'False' as an input
        # to denote that the player is playing for the first time.
        main_logic()

        clear_table(output_table)
        os.system("clear")
        game_header()

        # call function play_or_play_again() to check if the player wants to continue playing or quit
        # argument True denotes this is a game replay
        play_game = play_or_play_again(True)

    # if the user quits the game, print score board
    score_board(game)
