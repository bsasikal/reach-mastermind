from score_board import *

YES_NO_DICT = {'Y': 1, 'N': 1}


# Function to accept & validate player's name as input
def get_input_name():
    player_name = ''
    while not player_name.isalnum():
        player_name = str(input("Enter your Name: "))

    return player_name


# Function that decides if user wants to continue playing game or not
def play_or_play_again(replay):
    # sets a string to differentiate the input string
    # from "playing for first time" to "playing again"
    if not replay:
        fill_string = ''
    else:
        fill_string = ' again'

    # takes player's input and decides whether to continue with the game or exit.
    play_game = ''

    while play_game not in YES_NO_DICT:
        play_game = input('Do you want to play{}? Enter "Y" or "N":'.format(fill_string)).upper()

    return play_game


# Function that lets you choose the game complexity
# Level 1: Easy - You have to guess a 3 digit number
# Level 2: Normal - You have to guess a 4 digit number
# Level 3: Hard - You have to guess a 5 digit number
def choose_game_complexity():
    complexity = ''
    while complexity not in COMPLEXITY_DICT:
        complexity = str(input("Enter the number of digits you want to guess (3 or 4 or 5): "))

    return complexity


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
    return guess


def calculate_count_and_count_with_position(random_num_list, guess_list):
    # count denotes the matching digits
    count = 0
    # count_with_position denoted the matching digits and position
    count_with_position = 0

    copy_random_num_list = random_num_list[:]

    # loop through every digit in guessed number
    # to calculate count and count_with_position
    for idx in range(len(guess_list)):
        # run the players guess against the dictionary
        # and increment count ==> Matching digits
        # if guess_list[idx] in random_num_dict_clone and random_num_dict_clone[guess_list[idx]] != 0:
        if guess_list[idx] in copy_random_num_list:
            count += 1
            # random_num_dict_clone[guess_list[idx]] -= 1
            copy_random_num_list.remove(guess_list[idx])

        # compare index to index of random number and player's guess
        # and increment count_with_position ==> Matching digits and position
        if guess_list[idx] == random_num_list[idx]:
            count_with_position += 1

    return count, count_with_position
