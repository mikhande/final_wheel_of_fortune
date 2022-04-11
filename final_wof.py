#Wheel of Fortune

#Definitions
import random

# from regex import P

file_path = (r'Assessments\Wheel of Fortune\words.txt')

def random_word(fname):
    word_dictionary = open("words.txt", "r")
    the_word = random.choice(word_dictionary.read().split())
    word_dictionary.close()
    print(the_word)
    return the_word

the_word = random_word('words.txt')

the_word_list = list(the_word)

correct_letters = []

for char in the_word: # for the character in the word, it will change the blank spaces to include the new guessed letter
        correct_letters.append("_")

guesses_made = []

vowels = ['a','e','i','o','u']

consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

#This is the wheel based off photo sent in chat
the_wheel =  [200, 400, 250, 150, 400, 600, 250, 350, 750, 800, 300, 200, 100, 500, 400, 300, 200, 700, 200, 150, 450, "BANKRUPTCY", "Lose a Turn"]

wheel_choice = random.choice(the_wheel)

player_bank = 0

rounds = 0

def add_round():
    global rounds
    rounds +1

player1_turn = False
player2_turn = True
player3_turn = True

p1_bank = 0
p2_bank = 0
p3_bank = 0

pbanks = [p1_bank, p2_bank, p3_bank]


#Functions section

#Spinning the wheel
def spin_wheel():
    # global player1_turn
    # global player2_turn
    global player_bank
    wheel_choice = random.choice(the_wheel)
    print("You landed on: " + str(wheel_choice))
    if wheel_choice == "BANKRUPTCY":
            print("Oh no! You landed on BANKRUPTCY and lost all your money...")
            player_bank = 0
            # player2_turn = False
            # player1_turn = True
            print("Your player bank is now: " + str(player_bank))
    elif wheel_choice == "Lose a Turn":
        # player2_turn = False
        # player1_turn = True
        print("Oops, you lost a turn.")
    else:
        player_bank += wheel_choice
        print("Nice! You now have the opportunity to make a guess.")
        # guess_consonant()



#Guessing a consonant

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
            player_bank + (wheel_choice * the_word_list.count(consonant_guess))
            print(player_bank)
            print('That letter is in the word! That means you have won: $' + str(player_bank))
            print(correct_letters)
        elif '_' not in correct_letters: #This is if you have guessed the full word by guessing letters 
            player_bank = (player_bank + wheel_choice * consonant_guess.count(correct_letters))
            print("Congratulations, the word was " + str(the_word) + ". You got it! Your bank is now: $" + (player_bank))
        elif consonant_guess != correct_letters:
            guesses_made.append(consonant_guess)
            print("Sorry, that was not in the word. It's the next player's turn.")
        elif consonant_guess in guesses_made:
            print("You've already guessed that! Here are the guesses you have made: " + str(guesses_made))
    else:
        print("That's not a consonant. Please try again.")
        guess_consonant()

#Guessing a vowel

def guess_vowel():
    global player_bank
    global vowel_guess
    player_bank -= 250
    print(player_bank)
    vowel_guess = input("$250 has been deducted from your bank. Please guess a vowel: ")
    for position in range(len(the_word_list)):
        if the_word_list[position] == vowel_guess:
            correct_letters[position] = vowel_guess
    if vowel_guess in the_word and '_' in correct_letters:
        print("That letter is in the word!")
        guesses_made.append(vowel_guess)
        print(correct_letters)
    elif '_' not in correct_letters:
        print("Congratulations, the word was " + str(the_word) + ". You got it!")
    elif vowel_guess != correct_letters:
        print("Sorry, that's not part of the word.")
    elif vowel_guess not in vowels:
        print("That's not a vowel. Try again.")

#Trying to solve the puzzle
def puzzle():
    global puzzle_guess
    puzzle_guess = input("Good luck! Please type in the word: ")
    if puzzle_guess.isalpha():
        if puzzle_guess == the_word:
            add_round()
            print("Congratulations, you got it! The word was " + str(the_word.upper()))
        elif puzzle_guess != the_word:
            print("Sorry, that's not it!")
    else: 
        print("That's not a word... Try again.")

#Round 3 definition
def round3():
    global given_letters
    given_letters = ['r','s','t','l','n','e']
    for position in range(len(the_word_list)):
        if the_word_list[position] == given_letters:
            correct_letters[position] = given_letters
    while rounds == 2:
        print("Congratulations on making it to round 3!")
        print("Here is your new word:" + str(correct_letters))
        print("")


#Game play

while rounds == rounds <= 1:
    print("Welcome to WHEEL OF FORTUNE!")
    print("Here is your word: " + str(correct_letters))
    print(the_word)

    #Player 1 round 1
    while player1_turn == False:
        # print("It is WHEEL OF FORTUNE! Welcome, Player 1, here is the word: " + str(correct_letters))
        first_spin = input("Player 1, to spin the wheel, type 'S': ") 
        first_spin.upper()
        if first_spin == "s": #Spin the wheel
            spin_wheel()
            if wheel_choice == "BANKRUPTCY" and wheel_choice == "Lose a Turn": #If bankrupt or lose a turn, it's the next player's turn
                player2_turn = False
                player1_turn = True
                print("Sorry player 1.. You lost your turn.")
            else:
                guess_consonant()
                if consonant_guess in the_word:
                    p1_bank = p1_bank + player_bank
                if consonant_guess not in the_word: #if the guess wrong, next player's turn
                    player2_turn = False
                    player1_turn = True
                if p1_bank >= 250: #Over 250 in the bank allows you to buy a vowel
                    vowel_question = input("You can now spin the wheel again, buy a vowel or guess the puzzle. A vowel costs $250. If wheel type 'W', for vowel type 'V,' if guess the puzzle type 'P': ")
                    vowel_question.upper()
                    if vowel_question == "v":
                        guess_vowel()
                        p1_bank = player_bank
                        if vowel_guess not in the_word:
                            player2_turn = False
                            player1_turn = True
                        
                    elif vowel_question == "p":
                        puzzle()
                        if puzzle_guess == the_word:
                            player2_turn = False
                            player1_turn = True
                            # break
                    elif vowel_question == "w":
                        spin_wheel()
                elif player_bank < 250: #less than 250 in the bank, no option to buy a vowel
                    last_response = input("You can now spin the wheel again or guess the puzzle. Type 'W' for Wheel and 'P' for Puzzle: ")
                    last_response.upper()
                    if last_response == "p":
                        puzzle()
                        if puzzle_guess == the_word:
                            break
                    elif last_response == "w":
                        spin_wheel()
        else:
            print("Please type 'S': ")

    #Player 2
    while player2_turn == False:
        first_spin = input("Player 2, to spin the wheel, type 'S': ")
        first_spin.upper()
        if first_spin == "s":
            spin_wheel()
            if wheel_choice == "BANKRUPTCY" or wheel_choice == "Lose a Turn":
                player3_turn = False
                player2_turn = True
                print("Sorry player 2.. You lost your turn.")
            else:
                #guess_consonant()
                p1_bank = player_bank
                if consonant_guess not in the_word:
                    player3_turn = False
                    player2_turn = True
                if p1_bank >= 250:
                    vowel_question = input("You can now buy spin the wheel again, buy a vowel or guess the puzzle. A vowel costs $250. If wheel type 'W', for vowel type 'V,' if guess the puzzle type 'P': ")
                    vowel_question.upper()
                    if vowel_question == "v":
                        guess_vowel()
                        p1_bank = player_bank
                        if vowel_guess not in the_word:
                            player3_turn = False
                            player2_turn = True
                        
                    elif vowel_question == "p":
                        puzzle()
                        if puzzle_guess == the_word:
                            player3_turn = False
                            player2_turn = True
                            break
                    elif vowel_question == "w":
                        spin_wheel()
                else:
                    last_response = input("You can now spin the wheel again or guess the puzzle. Type 'W' for Wheel and 'P' for Puzzle: ")
                    last_response.upper()
                    if last_response == "p":
                        puzzle()
                        if puzzle_guess == the_word:
                            player3_turn = False
                            player2_turn = True
                    elif last_response == "w":
                        spin_wheel()
        else:
            print("Please type 'S': ")

        #Player 3 round 1
    while player3_turn == False:
        # print("It is WHEEL OF FORTUNE! Welcome, Player 1, here is the word: " + str(correct_letters))
        first_spin = input("Player 3, to spin the wheel, type 'S': ") 
        first_spin.upper()
        if first_spin == "s": #Spin the wheel
            spin_wheel()
            if wheel_choice == "BANKRUPTCY" and wheel_choice == "Lose a Turn": #If bankrupt or lose a turn, it's the next player's turn
                player3_turn = True
                print("Sorry player 1.. You lost your turn.")
            else:
                guess_consonant()
                if consonant_guess in the_word:
                    p3_bank = p3_bank + player_bank
                if consonant_guess not in the_word: #if the guess wrong, next player's turn
                    player3_turn = True
                if p1_bank >= 250: #Over 250 in the bank allows you to buy a vowel
                    vowel_question = input("You can now spin the wheel again, buy a vowel or guess the puzzle. A vowel costs $250. If wheel type 'W', for vowel type 'V,' if guess the puzzle type 'P': ")
                    vowel_question.upper()
                    if vowel_question == "v":
                        guess_vowel()
                        p1_bank = player_bank
                        if vowel_guess not in the_word:
                            player3_turn = True
                        
                    elif vowel_question == "p":
                        puzzle()
                        if puzzle_guess == the_word:
                            player3_turn = True
                            # break
                    elif vowel_question == "w":
                        spin_wheel()
                elif player_bank < 250: #less than 250 in the bank, no option to buy a vowel
                    last_response = input("You can now spin the wheel again or guess the puzzle. Type 'W' for Wheel and 'P' for Puzzle: ")
                    last_response.upper()
                    if last_response == "p":
                        puzzle()
                        if puzzle_guess == the_word:
                            player3_turn = True
                    elif last_response == "w":
                        spin_wheel()
        else:
            print("Please type 'S': ")

else: 
    round3()