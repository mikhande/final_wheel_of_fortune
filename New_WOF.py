#Wheel of Fortune

#Definitions
import random

from sqlalchemy import true

# from regex import P

file_path = (r'Assessments\Wheel of Fortune\words.txt')

def random_word(fname):
    global the_word
    word_dictionary = open("words.txt", "r")
    the_word = random.choice(word_dictionary.read().split())
    word_dictionary.close()
    print(the_word)
    return the_word

def get_word():
    global the_word
    global the_word_list
    global correct_letters
    the_word = random_word('words.txt')

    the_word_list = list(the_word)

    correct_letters = []

    for char in the_word: # for the character in the word, it will change the blank spaces to include the new guessed letter
        correct_letters.append("_")

guesses_made = []

vowels = ['a','e','i','o','u']

consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

#This is the wheel based off photo sent in chat
the_wheel =  ["BANKRUPTCY", "Lose a Turn", 200, 400, 250, 150, 400, 600, 250, 350, 750, 800, 300, 200, 100, 500, 400, 300, 200, 700, 200, 150, 450]

player_bank = 0

player1 = "p1_bank"
player2 = "p2_bank"
player3 = "p3_bank"

p1_bank = 0
p2_bank = 0
p3_bank = 0

player_names = {p1_bank: "player 1", p2_bank: "player 2", p3_bank: "player 3"}

rounds = 0
player_turn = 0

guess = False

p1_turn = True
p2_turn = False
p3_turn = False

def add_turn():
    global player_turn
    player_turn +1


def add_round():
    global rounds
    rounds = rounds + 1

def spin_wheel():
    global player_bank
    global wheel_choice
    wheel_choice = random.choice(the_wheel)
    print("You landed on: " + str(wheel_choice))
    if wheel_choice == "BANKRUPTCY":
            print("Oh no! You landed on BANKRUPTCY and lost all your money...")
            player_bank = 0
            add_turn()
            print("Your player bank is now: " + str(player_bank))
    else:
        player_bank = wheel_choice
        print("Nice! You now have the opportunity to make a guess.")
        guess_consonant()

def guess_consonant():
    global player_bank
    global consonant_guess
    print(correct_letters)
    consonant_guess = input("Guess a consonant: ")
    for position in range(len(the_word_list)):
        if the_word_list[position] == consonant_guess:
            correct_letters[position] = consonant_guess
    if consonant_guess in consonants: 
        if consonant_guess in the_word and '_' in correct_letters: #This is if you have guessed a letter in the word but haven't guessed the full word
            guesses_made.append(consonant_guess)
            player_bank = (player_bank * the_word_list.count(consonant_guess))
            print(player_bank)
            print('That letter is in the word! That means you have won: $' + str(player_bank))
            print(correct_letters)
        elif '_' not in correct_letters: #This is if you have guessed the full word by guessing letters 
            player_bank = (player_bank * consonant_guess.count(correct_letters))
            print("Congratulations, the word was " + str(the_word) + ". You got it! Your bank is now: $" + (player_bank))
            add_round()
        elif consonant_guess != correct_letters:
            guesses_made.append(consonant_guess)
            print("Sorry, that was not in the word. It's the next player's turn.")
        elif consonant_guess in guesses_made:
            print("You've already guessed that! Here are the guesses you have made: " + str(guesses_made))
    else:
        print("That's not a consonant. Please try again.")
        guess_consonant()

def under_250():
    if player_bank < 250:
    # p1_bank < 250: #less than 250 in the bank, no option to buy a vowel
        last_response = input("You can now spin the wheel again or guess the puzzle. Type '1' for Wheel and '2' for Puzzle: ")
        if last_response == "2":
            puzzle()
            if puzzle_guess == the_word:
                add_round()
                guess = True
            else:
                player1_turn = False
                player2_turn = True
        elif last_response == "1":
            spin_wheel()
            if wheel_choice == "BANKRUPTCY" or wheel_choice == "Lose a Turn": #If bankrupt or lose a turn, it's the next player's turn
                p1_bank = player_bank
                print("player 1 bank is now: " + str(p1_bank))
                player2_turn = True
                player1_turn = False
                print("Sorry player 1.. You lost your turn.")


while guess == False and rounds < 2:

    print("Welcome to rounds 1 & 2!")

    get_word()

    while p1_turn == True :
        first_spin = input("Player 1, to spin the wheel, type '1': ")
        if first_spin == "1": #Spin the wheel
                spin_wheel()
                p1_bank += player_bank
                if wheel_choice == "BANKRUPTCY" or wheel_choice == "Lose a Turn":
                    print("Your bank is at: " + str(p1_bank))
                    p1_turn = False
                    p2_turn = True