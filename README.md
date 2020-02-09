# MasterMind game

Mastermind is a classic board game for two players, a code-maker and a code-breaker. Here, the computer is the code-maker and the user/player will be the code-breaker. 

Computer will generate a random number depending on the difficulty level that the player chooses.
- If the player inputs ‘1’ when prompted, then the program generates a random 3 digit number and the player have to guess that 3 digit number (Easy)
- If the player inputs ‘2’, then the program generates a random 4 digit number and the player have to guess that 4 digit number (Normal)
- If the player inputs ‘3’, then the program generates a random 5 digit number and the player have to guess that 5 digit number (Hard)

The program uses random generator API to generate random numbers. This API takes number of digits as one of the inputs which is set by the program based on the difficulty level before the API call.

The computer also gives feedback after every guess that the player makes. It gives feedback on how many digits matches and how many digits and position matches. With each guess the player makes, he/she can use those feedback as clues and get closer to the random number.

The player gets 10 attempts to crack the program generated random number.

At the end of the game, the program will display a scoreboard, with details on how many games played, its complexity level, the result of the game and the number of attempts of that particular player.

## Getting Started

Please follow these instructions to get the project running on your local machine.

### Prerequisites

You will need to install the following:
```
- Python 3.7.4

- Python library - requests
	sudo pip3.7 install --upgrade pip
	sudo pip3 install requests

- Python library - PrettyTable
	sudo pip3 install PrettyTable
```

### Installation

Grab a copy of the program by entering the following into your terminal and cd into the repository.

```
git clone https://github.com/bsasikal/reach-mastermind.git
```

Once you have finished installing everything, you are ready to run the game.

#### How to run the game
	
Move back to the root directory of the repository and execute

```
python mastermind.py
```

The program first prompts the player to enter a name:
Once entered, the player should see a screen like this

![start] (images/table welcome.png?raw=true)

Once you choose the complexity level, it lets the player enter their “guess”.

![alt text] [https://github.com/bsasikal/reach-mastermind/tree/master/images/start.png]

As you play, the player will be able to see their previous guesses along with the feedback.

![alt text] [https://github.com/bsasikal/reach-mastermind/tree/master/images/feedback1.png]

For the last 3 guesses, you will receive a warning with the number of attempts left to guess the number.

![alt text] [https://github.com/bsasikal/reach-mastermind/tree/master/images/warning.png]

After the player exhausts all the 10 attempts, the player will be able to see all his 10 guesses, the computer’s feedback and the random number.

![alt text] [https://github.com/bsasikal/reach-mastermind/tree/master/images/feedback2.png]

If the player guesses the number correctly, the player will still be able to see all his 10 guesses, the computer’s feedback.

![alt text] [https://github.com/bsasikal/reach-mastermind/tree/master/images/feedback3.png]

At the end of the game, a scoreboard will be shown for that player, with the complexity level, result and number of attempts of each game played.

![alt text] [https://github.com/bsasikal/reach-mastermind/tree/master/images/result.png]

### Extension
- Added functionality for the player to set complexity level of the game
- Scoreboard at the end of the game







