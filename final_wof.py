#Wheel of Fortune

#Definitions
import random

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

wheel_choice = random.choice(the_wheel)

player_bank = 0

p1_bank = 0
p2_bank = 0
p3_bank = 0

rounds = 0

def add_round():
    global rounds
    rounds = rounds + 1



#Functions section

#Spinning the wheel
def spin_wheel():
    global player_bank
    wheel_choice = random.choice(the_wheel)
    print("You landed on: " + str(wheel_choice))
    if wheel_choice == "BANKRUPTCY":
            print("Oh no! You landed on BANKRUPTCY and lost all your money...")
            player_bank = 0
            print("Your player bank is now: " + str(player_bank))
    elif wheel_choice == "Lose a Turn":
        print("Oops, you lost a turn.")
    else:
        player_bank = wheel_choice
        print("Nice! You now have the opportunity to make a guess.")
        guess_consonant()



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

#Guessing a vowel

def guess_vowel():
    global player_bank
    global vowel_guess
    player_bank -= 250
    print("Your bank is now at: $" + str(player_bank))
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
            print(rounds)
            print("Congratulations, you got it! The word was " + str(the_word.upper()))
            print("We will begin Round 2 now. Good luck!")
        elif puzzle_guess != the_word:
            print("Sorry, that's not it!")
    else: 
        print("That's not a word... Try again.")

#Round 3 definition
def round3():
    global player   
    global given_letters
    player_names = {p1_bank: "player 1", p2_bank: "player 2", p3_bank: "player 3"}
    player = (player_names[max(player_names)])

    get_word()
    print("Welcome to round 3: " + (player))

    given_letters = ['r','s','t','l','n','e']
    for position in range(len(the_word_list)):
        if the_word_list[position] == given_letters:
            correct_letters[position] = given_letters
    print("Your word is: " + (the_word))




# Defining rounds 1 & 2. Code is repeated for players 1, 2, and 3. Gameplay starts in a while loop after this block of code. 
def round1_2():
    global p1_bank
    global p2_bank
    global p3_bank
    player1_turn = True
    player2_turn = False
    player3_turn = False

    guess = False



    print(p1_bank, p2_bank, p3_bank)

  
    while guess == False:

#Player 1's turn
        while player1_turn == True:
            get_word()
        
            print("Welcome to WHEEL OF FORTUNE! Rounds 1 & 2")
            print("Here is your word: " + str(correct_letters))
            print(the_word)

            first_spin = input("Player 1, to spin the wheel, type '1': ") 
            if first_spin == "1": #Spin the wheel
                spin_wheel()
                if wheel_choice == "BANKRUPTCY" or wheel_choice == "Lose a Turn": #If bankrupt or lose a turn, it's the next player's turn
                    p1_bank = player_bank
                    print("player 1 bank is now: " + str(p1_bank))
                    player2_turn = True
                    player1_turn = False
                    print("Sorry player 1.. You lost your turn.")
                else:
                    if consonant_guess not in the_word: #if the guess is wrong, next player's turn
                        player2_turn = True
                        player1_turn = False
                    elif consonant_guess in the_word:
                        p1_bank = p1_bank + player_bank
                        print("player 1 bank = " + str(p1_bank))
                        if p1_bank >= 250: #Over 250 in the bank allows you to buy a vowel
                            vowel_question = input("You can now spin the wheel again, buy a vowel or guess the puzzle. A vowel costs $250. If wheel type '1', for vowel type '2,' if guess the puzzle type '3': ")
                            if vowel_question == "2": #Player can guess a vowel
                                guess_vowel()
                                p1_bank = player_bank
                                if vowel_guess not in the_word:
                                    player2_turn = True
                                    player1_turn = False   
                            elif vowel_question == "3": #Player can guess the puzzle
                                puzzle()
                                if puzzle_guess == the_word:
                                    add_round()
                                    guess = True
                                else:
                                    player1_turn = False
                                    player2_turn = True
                            elif vowel_question == "1":
                                spin_wheel()
                                if wheel_choice == "BANKRUPTCY": #If bankrupt or lose a turn, it's the next player's turn
                                    p1_bank = player_bank
                                    print("player 1 bank is now: " + str(p1_bank))
                                    player2_turn = True
                                    player1_turn = False
                                    print("Sorry player 1.. You lost your turn.")
                                elif wheel_choice == "Lose a Turn":
                                    p1_bank = player_bank
                                    player2_turn = True
                                    player1_turn = False
                                else:
                                    if consonant_guess not in the_word: #if the guess is wrong, next player's turn
                                        player2_turn = True
                                        player1_turn = False
                                    elif consonant_guess in the_word:
                                        p1_bank = p1_bank + player_bank
                                        print("player 1 bank = " + str(p1_bank))
                            else:
                                print("Please type either 1, 2, or 3.")
                        elif p1_bank < 250:
                            # p1_bank < 250: #less than 250 in the bank, no option to buy a vowel
                            last_response = input("You can now spin the wheel again or guess the puzzle. Type '1' for Wheel and '2' for Puzzle: ")
                            last_response.upper()
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
                                else:
                                    if consonant_guess not in the_word: #if the guess is wrong, next player's turn
                                        player2_turn = True
                                        player1_turn = False
                                    elif consonant_guess in the_word:
                                        p1_bank = p1_bank + player_bank
                                        print("player 1 bank = " + str(p1_bank))
                                print("Please type either 1 or 2.")
            else:
                print("Please type '1: ")

    #Player 2
        while player2_turn == True:
            print(p1_bank, p2_bank, p3_bank)
            first_spin = input("Player 2, to spin the wheel, type '1': ")
            if first_spin == "1":
                spin_wheel()
                if wheel_choice == "BANKRUPTCY" or wheel_choice == "Lose a Turn": #If bankrupt or lose a turn, it's the next player's turn
                    p2_bank = player_bank
                    print("player 2 bank is now: " + str(p1_bank))
                    player3_turn = True
                    player2_turn = False
                    print("Sorry player 2.. You lost your turn.")
                else:
                    if consonant_guess not in the_word: #if the guess is wrong, next player's turn
                        player3_turn = True
                        player2_turn = False
                    elif consonant_guess in the_word:
                        p2_bank = p2_bank + player_bank
                        print("player 1 bank = " + str(p2_bank))
                        if p2_bank >= 250:
                            vowel_question = input("You can now buy spin the wheel again, buy a vowel or guess the puzzle. A vowel costs $250. If spin the wheel type '1', for vowel type '2', if guess the puzzle type '3': ")
                            if vowel_question == "2":
                                guess_vowel()
                                p2_bank = player_bank
                                if vowel_guess not in the_word:
                                    player3_turn = True
                                    player2_turn = False    
                            elif vowel_question == "3":
                                puzzle()
                                if puzzle_guess == the_word:
                                    add_round()
                                    guess = True
                                    player2_turn = False
                                else:
                                    player2_turn = False
                                    player3_turn = True
                            elif vowel_question == "1":
                                spin_wheel()
                        elif p2_bank < 250: #less than 250 in the bank, no option to buy a vowel
                            last_response = input("You can now spin the wheel again or guess the puzzle. Type '1' for Wheel and '2' for Puzzle: ")
                            last_response.upper()
                            if last_response == "2":
                                puzzle()
                                if puzzle_guess == the_word:
                                    add_round()
                                    guess = True
                                else:
                                    player2_turn = False
                                    player3_turn = True
                            elif last_response == "1":
                                spin_wheel()
                                if wheel_choice == "BANKRUPTCY" or wheel_choice == "Lose a Turn": #If bankrupt or lose a turn, it's the next player's turn
                                    p2_bank = player_bank
                                    print("player 2 bank is now: " + str(p1_bank))
                                    player3_turn = True
                                    player2_turn = False
                                    print("Sorry player 2.. You lost your turn.")
                                else:
                                    if consonant_guess not in the_word: #if the guess is wrong, next player's turn
                                        player3_turn = True
                                        player2_turn = False
                                    elif consonant_guess in the_word:
                                        p2_bank = p2_bank + player_bank
                                        print("player 2 bank = " + str(p1_bank))
            else:
                print("Please type '1': ")

    #Player 3
        while player3_turn == True:
            print(p1_bank, p2_bank, p3_bank)
            first_spin = input("Player 3, to spin the wheel, type '1': ")
            first_spin.upper()
            if first_spin == "1":
                spin_wheel()
                if wheel_choice == "BANKRUPTCY" or wheel_choice == "Lose a Turn":
                    p3_bank = player_bank
                    player1_turn = True
                    player3_turn = False
                    print("Sorry player 3.. You lost your turn.")
                else:
                    if consonant_guess not in the_word:
                        player1_turn = True
                        player3_turn = False
                    elif consonant_guess in the_word:
                        p3_bank = p3_bank + player_bank
                        print("player 2 bank = " + str(p3_bank))
                        if p3_bank >= 250:
                            vowel_question = input("You can now buy spin the wheel again, buy a vowel or guess the puzzle. A vowel costs $250. If wheel type '1', for vowel type '2,' if guess the puzzle type '3': ")
                            if vowel_question == "2":
                                guess_vowel()
                                p3_bank = player_bank
                                if vowel_guess not in the_word:
                                    player1_turn = True
                                    player3_turn = False    
                            elif vowel_question == "3":
                                puzzle()
                                if puzzle_guess == the_word:
                                    add_round()
                                    guess = True
                                    player3_turn = False
                                else:
                                    player3_turn = False
                                    player1_turn = True
                            elif vowel_question == "1":
                                spin_wheel()
                        elif p3_bank < 250: #less than 250 in the bank, no option to buy a vowel
                            last_response = input("You can now spin the wheel again or guess the puzzle. Type '1' for Wheel and '2' for Puzzle: ")
                            last_response.upper()
                            if last_response == "2":
                                puzzle()
                                if puzzle_guess == the_word:
                                    add_round()
                                    guess = True
                                else:
                                    player1_turn = True
                                    player3_turn = False
                            elif last_response == "1":
                                spin_wheel()
                                if wheel_choice == "BANKRUPTCY" or wheel_choice == "Lose a Turn": #If bankrupt or lose a turn, it's the next player's turn
                                    p3_bank = player_bank
                                    print("player 3 bank is now: " + str(p3_bank))
                                    player1_turn = True
                                    player3_turn = False
                                    print("Sorry player 3.. You lost your turn.")
                                else:
                                    if consonant_guess not in the_word: #if the guess is wrong, next player's turn
                                        player1_turn = True
                                        player3_turn = False
                                    elif consonant_guess in the_word:
                                        p3_bank = p3_bank + player_bank
                                        print("player 3 bank = " + str(p3_bank))
            else:
                print("Please type '1': ")


#game play

while rounds < 2 :
    round1_2()
else:
     round3()