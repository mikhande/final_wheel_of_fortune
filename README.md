# final_wheel_of_fortune
This Wheel of Fortune game is a project for Module 6 on the Basics of Python.
It includes the python file of the game, the word list file, and a plans folder for the pseudo code.

Details about the rules:

The main point of the game is to make as much money as you can while guessing letters that make up a word.

Players are able to make money by spinning a wheel. The section of wheel they land on determines how much money they can get for each of their consonant guesses. Below are the possible outcomes of spinning the wheel.

The wheel lands on a number:
Player guesses a consonant that is in the puzzle: consonant (s) are revealed and they get the money on the wheel (Note: It does not matter how many times the consonant appears in the word. As long as the consonant appears at least once, they get the entire value of their wheel spin.)
Player guesses a consonant that is NOT in the puzzle: their turn ends and they get no money
The wheel lands on BANKRUPT:
Player's bank goes to 0 and their turn ends
If a player successfully guesses a consonant, they also get an opportunity to "buy a vowel", which costs $250. They can continue to buy vowels as long as the vowels appear. If a word is down to vowels, each round is played with players being able to buy vowels.

At any point, a player can guess the answer. For this particular turn-based approach, a player should only attempt to guess the answer on their turn. If they successfully guess the answer, they win the round. If they do not successfully guess the answer, that consumes their turn.

For our game, there are 2 rounds with 3 players. The player with the most money at the end of round 2 goes on to round 3.

The round is over when the answer is guessed.
