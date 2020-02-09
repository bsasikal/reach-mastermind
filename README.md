This is a command line MasterMind game created by Sasikala Balaraman for LinkedIn Reach program

# MasterMind game

## Introduction

Mastermind is a classic board game for two players, a code-maker and a code-breaker. Here, the application is the code-maker and the user/player will be the code-breaker. 

The application will generate a random number depending on the difficulty level that the player chooses.
- Level 1 - Easy: When prompted, player inputs ‘1’ and the application generates a 3 digit random number
- Level 2 - Normal: When prompted, player inputs ‘2’ and the application generates a 4 digit random number
- Level 3 - Hard: When prompted, player inputs ‘3’ and the application generates a 5 digit random number

The application uses a random generator [API](https://www.random.org/clients/http/api/) to generate random numbers. This API takes number of digits as one of the inputs and it will be decided by the application based on the difficulty level chosen by the player.

The application also gives feedback after every guess that the player makes. It gives feedback on 
- the number of matching digits and 
- the number of matching digits and the matching position

With each guess the player makes, he/she can use the feedback as clues and use it to guess the random number.

The player gets 10 attempts to guess the random number.

At the end of the game, the application will display a scoreboard, with details on number of games played, its complexity level, the result of the game and the number of attempts.

## Getting Started

Please follow these instructions to run the application on your local machine.

## Requirements

This is a Python based application and it requires the following libraries:
```
- Python 3.7.4

- Python library - "requests"
	sudo pip3.7 install --upgrade pip
	sudo pip3 install requests

- Python library - "PrettyTable"
	sudo pip3 install PrettyTable
```

## Project installation

Clone the repository by running tbe below command from your terminal

```
git clone https://github.com/bsasikal/reach-mastermind.git
```

## How to Run
	
Execute the following command to run the application.

```
cd reach-mastermind/src && python mastermind.py
```

The application first prompts for you to enter your name:

Once entered, you should see a screen like below

![welcome](./images/welcome.png?raw=true)

After you choose the complexity level, the application lets you to enter your “guess”. You will get 10 attempts to guess the number.

![start](./images/start.png?raw=true)

As you play, you will be able to see the previous guesses along with the feedback.

![feedback](./images/feedback1.png?raw=true)

For the last 3 guesses, you will receive a warning with the number of remaining attempts to guess the number.

![warning](./images/warning.png?raw=true)

After you exhaust all the attempts, you will be able to see all 10 guesses, the feedback and the random number.

![feedback](./images/feedback2.png?raw=true)

If you guess the number correctly, you will still be able to see all 10 guesses and the feedback.

![feedback](./images/feedback3.png?raw=true)

At the end of the game, a scoreboard will be shown with the complexity level, final result and the number of attempts for each game played.

![result](./images/result.png?raw=true)

## Extension
In addition to the MVP asked, I have implemented the following additional features in the game.

- Player can choose the complexity level (1-easy or 2-normal or 3-hard) of the game
- Display scoreboard at the end of the game

## Running the tests
Unit test is located in reach-mastermind/src in the file mastermind_test.py

To run the tests, execute the following command from the $PROJECT_HOME/src directory

```
python -m unittest mastermind_test.py -b
```

## Project Enhancements

#### Functionality:
- Add a timer to track the time spent for each guess attempts and the total time spent to complete the game
- Rank the success/failure attempts 
- Dynamically change the difficulty of the problem based on the complexity level
- Provide a leaderboard (handle multiple user sessions and store the results in a database)
- Enhance the usability by adding a rich user interface (web/mobile client)

#### Testing
- Add additional mock test to increase the code coverage

#### Packaging:
- Update installation scripts to use Python setup scripts setup.py & requirements.txt


## Author
Created by Sasikala Balaraman






