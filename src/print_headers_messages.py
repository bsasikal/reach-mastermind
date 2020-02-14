import os


# Function to print the game header,
# to explain the complexity level choices,
# to specify game rules,
# to explain the feedback variables - Matching Digits & Matching Digits and Position.
def game_header():
    os.system("clear")
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


# Function that prints success message
# with the number of attempts the player took to guess the correct number
# calls function play() to check if the player wants to continue playing or quit
def success_message(attempt):
    print("\n##############################################################################")
    print("\t\tCONGRATULATIONS!! You are a Mastermind!!")
    print("\t    It took you only", attempt, "attempts to guess the number.")
    print("##############################################################################")

    input("Press Enter to continue...")


# Function that prints failure message
# if the player could not guess the correct number in 10 attempts
# calls function play() to check if the player wants to continue playing or quit
def sorry_message(random_num_list):
    print("\n#############################################################################")
    print("\t You have maxed out the number of attempts...Sorry!!!")
    print("\t\t The random number is", ''.join(map(str, random_num_list)))
    print("#############################################################################\n")

    input("Press Enter to continue...")

