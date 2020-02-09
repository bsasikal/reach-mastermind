import random
import os
import requests
import copy
from colorama import Fore
from prettytable import PrettyTable

NO_OF_ATTEMPTS = 10


# class that stores details of all the games for score board
class Player:
    name = ''
    complexity = []
    result = []
    num_attempt = []

    def append_player_data(self, complexity, result, num_attempt):
        self.complexity.append(complexity)
        self.result.append(result)
        self.num_attempt.append(num_attempt)


# function that uses class Player and
# prints score board at the end of the game
def score_board():
    os.system("clear")
    print("\n###################################################")
    print("~~~~~~~~~~~~~~~~~~ MASTER MIND ~~~~~~~~~~~~~~~~~~~")
    print("###################################################\n")
    print("\t\t{}'s SCORE BOARD".format(player.name).upper())
    score_table = PrettyTable(['Game ID', 'Complexity', 'Result', 'No.of attempts'])

    game_id = 0
    for idx in range(len(player.complexity)):

        game_id += 1

        if player.complexity[idx] == 3:
            str_complexity = 'Easy'
        elif player.complexity[idx] == 4:
            str_complexity = 'Normal'
        elif player.complexity[idx] == 5:
            str_complexity = 'Hard'

        score_table.add_row([game_id, str_complexity, player.result[idx], player.num_attempt[idx]])

    print(score_table)
    print("\n\nGAME OVER!!!!!!")
    print("Nice playing {}. See you soon..!\n".format(player.name))
    input("\n\nPress Enter to continue...")
    os.system("clear")


# Function that calls Random Number Generator API
# to generate the random number combinations
# The argument 'complexity' decides the number of digits in random number
def generate_random_number(complexity):
    URL = "https://www.random.org/integers/"
    PARAM = {'num': complexity, 'min': '0', 'max': '7', 'col': '1', 'base': '10', 'format': 'plain', 'rnd': 'new'}

    r = requests.get(url=URL, params=PARAM)
    random_list = []

    for i in r.iter_lines():
        random_list.append(int(i))

    random_num = ''.join(map(str, random_list))
    return random_num, random_list


# Function to print the game header,
# to explain the complexity level choices,
# to specify game rules,
# to explain the feedback variables - Matching Digits & Matching Digits and Position.
def game_header():
    #os.system("clear")
    print("##############################################################################")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MASTER MIND ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("##############################################################################")
    print("GAME RULES:")
    print("\t - Choose the level of Complexity")
    print("\t\t Level 1: Easy (3 digits) \n\t\t Level 2: Normal (4 digits) \n\t\t Level 3: Hard (5 digits)")
    print("\t - Computer will randomly select a number depending on the complexity level")
    print("\t - You will have 10 attempts to guess the number combinations")
    print("\t - After each guess, the computer will provide the following feedback")
    print("\t     - \"Matching Digits\" - No of digits in your guess that \n \t \t \t matches the random number.")
    print("\t     - \"Matching Digits and Position\" - No of digits and its \n \t \t \t position in your guess that "
          "matches the random number.")
    print("##############################################################################")


# Function that lets you choose the game complexity
# Level 1: Easy - You have to guess a 3 digit number
# Level 2: Normal - You have to guess a 4 digit number
# Level 3: Hard - You have to guess a 5 digit number
def choose_game_complexity():
    selection = ''
    while selection not in ['1', '2', '3']:
        selection = str(input("Choose a Complexity Level (1 or 2 or 3): "))

    if selection == '1':
        complexity = 3
    elif selection == '2':
        complexity = 4
    elif selection == '3':
        complexity = 5

    return complexity


# Function that adds details of guesses and feedback to the table
# prints the table with added details
def add_row_to_table(output_table, sno, guess, count, count_with_position):
    output_table.add_row([sno, guess, count, count_with_position])
    print(output_table)


# Function that initializes the game / game replay
# takes player's input and decides whether to continue with the game or exit.
# takes player's input and decides the level of complexity in the game.
# creates a simple ASCII table to easily visualize the guesses and feedback
# calls the main function to proceed with the actual logic of the game
def play(replay):
    game_header()

    # sets a string to differentiate the input string
    # from "playing for first time" to "playing again" ...
    if not replay:
        fill_string = ''
    else:
        fill_string = ' again'

    # takes player's input and decides whether to continue with the game or exit.
    play_game = ''

    while play_game not in ['Y', 'N']:
        play_game = input('Do you want to play{}? Enter "Y" or "N":'.format(fill_string)).upper()

    # if the player wants to play
    if play_game.startswith('Y'):

        # accept player's input and decides his/her level of complexity in the game.
        complexity = choose_game_complexity()

        # create a simple ASCII table for visualizing the guesses and the feedback
        # using PrettyTable library
        output_table = PrettyTable(['Attempts', 'Your Guess', 'Matching Digits', 'Matching Digits and Position'])

        # call to the function with the actual logic of game
        main_logic(output_table, complexity)

    # if the player doesn't want to play
    elif play_game.startswith('N'):
        # print score board
        score_board()
        exit()


# Function that prints success message
# with the number of attempts the player took to guess the correct number
# calls function play() to check if the player wants to continue playing or quit
def success_message(attempt):
    print("\n##############################################################################")
    print("\t\tCONGRATULATIONS!! You are a Mastermind!!")
    print("\t    It took you only", attempt, "attempts to guess the number.")
    print("##############################################################################")

    input("Press Enter to continue...")

    # call function play() to check if the player wants to continue playing or quit
    # argument True denotes this is a game replay
    os.system("clear")
    play(True)


# Function that prints failure message
# if the player could not guess the correct number in 10 attempts
# calls function play() to check if the player wants to continue playing or quit
def sorry_message(random_num):
    print("\n#############################################################################")
    print("\t You have maxed out the number of attempts...Sorry!!!")
    print("\t\t The random number is", random_num)
    print("#############################################################################\n")

    input("Press Enter to continue...")

    # call function play() to check if the player wants to continue playing or quit
    # argument True denotes this is a game replay
    os.system("clear")
    play(True)


# Function that takes player's guessed number as input
# checks to ensure that the players guess contains only numbers
# checks to ensure that number of digits in guess number and random number matches
def guess_the_number(random_num_len):
    guess = ''
    guess_len = 0

    # check to ensure that the guessed number matches the number of digits in random number
    while guess_len != random_num_len or not guess.isdigit():
        guess = str(input("\nGuess the {} digit number:".format(random_num_len)))

        # check to ensure that the players guess contains only numbers
        while not guess.isdigit():
            guess = str(input("Numbers only please..! Guess a {} digit number:".format(random_num_len)))

        guess_len = len(guess)

    os.system("clear")
    game_header()
    return guess


# Function that has the core game logic
# get both random number and player's guess
# calculate count and count_with_position
# print guess and feedback to the table
def main_logic(output_table, complexity):
    # generate random number
    random_num, random_num_list = generate_random_number(complexity)
    random_num_len = len(random_num)

    # get the player's guess
    guess = guess_the_number(random_num_len)
    # convert the guessed number into a list
    guess_list = list(map(int, guess))

    # condition to check if the player's guess and random number are equal
    if guess == random_num:
        print("Great! You guessed the number in just 1 try!\n")
        player.append_player_data(complexity, 'Success', 1)
        success_message(1)
    else:
        # attempt variable initialized.
        # It will keep count of the number of tries the player takes to guess the number.
        attempt = 0

        random_num_dict = {}

        # loop through the random number and
        # create a dictionary with each digit as key and value set to 1
        # for digits with more than one occurrence, increment the value
        for num in random_num_list:
            if num in random_num_dict:
                random_num_dict[num] += 1
            else:
                random_num_dict[num] = 1

        random_num_dict_clone = {}

        # Loop for 10 attempts
        while attempt < NO_OF_ATTEMPTS:

            # copy random number dictionary to a temp dictionary
            random_num_dict_clone.clear()
            random_num_dict_clone = copy.deepcopy(random_num_dict)

            # increment the variable attempt
            attempt += 1
            # count denotes the matching digits
            count = 0
            # count_with_position denoted the matching digits and position
            count_with_position = 0

            # loop through every digit in guessed number
            # to calculate count and count_with_position
            for idx in range(len(guess_list)):

                # run the players guess against the dictionary
                # and increment count ==> Matching digits
                if guess_list[idx] in random_num_dict_clone and random_num_dict_clone[guess_list[idx]] != 0:
                    count += 1
                    random_num_dict_clone[guess_list[idx]] -= 1

                # compare index to index of random number and player's guess
                # and increment count_with_position ==> Matching digits and position
                if guess_list[idx] == random_num_list[idx]:
                    count_with_position += 1

            add_row_to_table(output_table, attempt, guess, count, count_with_position)

            # if the player guessed the right number
            if count == count_with_position and guess == random_num:
                # for score board
                player.append_player_data(complexity, 'Success', attempt)
                success_message(attempt)
                break

            # if the player maxed out 10 attempts
            if attempt == NO_OF_ATTEMPTS:
                # for score board
                player.append_player_data(complexity, 'Failed', attempt)
                sorry_message(random_num)
                break

            if 7 <= attempt < 9:
                print (Fore.RED + "\nWARNING: You now have only {} attempt(s) left to guess the number.... ".format(10-attempt) + Fore.RESET)
            elif attempt == 9:
                print(Fore.RED + "\nWARNING: Your FINAL chance to guess the number.... " + Fore.RESET)

            # guess the number again
            guess = guess_the_number(random_num_len)
            guess_list = list(map(int, guess))

    # call function play() to check if the player wants to continue playing or quit
    # argument True denotes this is a game replay
    os.system("clear")
    play(True)


# Main function
if __name__ == '__main__':
    # Create an object for class Player
    player = Player()

    os.system("clear")

    # accept player's name
    name = ''
    while not name.isalnum():
        name = str(input("Enter your Name: "))

    player.name = name.capitalize()

    os.system("clear")
    print("\nHello {}.. Welcome to the game!".format(player.name))

    # Calls the function play by passing boolean 'False' as an input
    # to denote that the player is playing for the first time.
    play(False)
