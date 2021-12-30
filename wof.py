# %%
import random
import json

s = open('wheel.txt')
segments = s.read().splitlines()
s.close()

f = open('words.txt')
word_choices = f.read().splitlines()
f.close()

def random_word():
    word = random.choice(word_choices)
    return word.upper()

consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
consonant_list = list(consonants)
vowels = 'AEIOU'
vowel_list = list(vowels)

player1 = 0
player2 = 0
player3 = 0
p1bank = 0
p2bank = 0
p3bank = 0
players = [player1,player2,player3]
playerList = [" Player 1", " Player 2", " Player 3"]
banks = [p1bank,p2bank,p3bank]


def spinWheel():
    spin = random.choice(segments) 
    return spin

def firstRounds(word):
    playerIndex = random.randint(0,2)
    print("Starting player:", playerList[playerIndex])
    display_word = "_" * len(word)
    is_guessed = False
    guessed_letters = []
    guessed_words = []
    print(display_word)
    print("\n")
    while is_guessed == False:
        spin = int(spinWheel())

        if spin == 0:
            players[playerIndex] = 0
            playerIndex = (playerIndex + 1) % 3
            print("Bankrupt! It is now " + playerList[playerIndex] + "'s turn.")
            print(display_word)
            print("\n")
        elif spin == 1:
            playerIndex = (playerIndex + 1) % 3
            print("Lose a turn! It is now" + playerList[playerIndex] + "'s turn.")
            print(display_word)
            print("\n")

        else:
            guess = input("Please guess a consonant: ").upper()
            if len(guess)==1 and guess.isalpha() and guess in consonant_list:
                if guess in guessed_letters:
                    print("That letter has already been guessed.")
                elif guess not in word:
                    playerIndex = (playerIndex + 1) % 3
                    print("That letter is not in the word. It is now" + playerList[playerIndex] + "'s turn.")
                    print(display_word)
                    print("\n")
                    guessed_letters.append(guess)

                else:
                    players[playerIndex] = players[playerIndex] + int(spin)
                    print("Correct,", guess, "is in the word! You currently have $",players[playerIndex])
                    guessed_letters.append(guess)
                    word_list = list(display_word)
                    letter_position = [i for i, letter in enumerate(word) if letter == guess]
                    for index in letter_position:
                        word_list[index] = guess
                    display_word = "".join(word_list)
                    print(display_word)
                    print("\n")
                    if "_" not in display_word:
                        is_guessed = True
                    ask_vowel = input("Would you like to buy a vowel? Y/N").upper()
                    if ask_vowel == 'Y':
                        guess = input("Please guess a vowel:").upper()
                        if len(guess)==1 and guess.isalpha() and guess in vowel_list:
                            if guess in guessed_letters:
                                print("That letter has already been guessed.")
                            elif guess not in word:
                                playerIndex = (playerIndex + 1) % 3
                                print("That letter is not in the word. It is now" + playerList[playerIndex] + "'s turn.")
                                print(display_word)
                                print("\n")
                                guessed_letters.append(guess)

                            else:
                                players[playerIndex] = players[playerIndex] - 250
                                print("Correct,", guess, "is in the word! You currently have $",players[playerIndex])
                                guessed_letters.append(guess)
                                word_list = list(display_word)
                                letter_position = [i for i, letter in enumerate(word) if letter == guess]
                                for index in letter_position:
                                    word_list[index] = guess
                                display_word = "".join(word_list)
                                print(display_word)
                                print("\n")
                                if "_" not in display_word:
                                    is_guessed = True
                                ask_word = input("Would you like to guess the word? Y/N").upper()
                                if ask_word == 'Y':
                                    guess = input("Please guess the word:").upper()
                                    if len(guess) == len(word) and guess.isalpha():
                                        if guess in guessed_words:
                                            print("You already guessed the word", guess)
                                        elif guess != word:
                                            print(guess, "is not the correct word.")
                                            guessed_words.append(guess)
                                        else:
                                            is_guessed = True
                                            display_word = word
                                    else:
                                        playerIndex = (playerIndex + 1) % 3
                                        print("Not a valid guess. It is now" + playerList[playerIndex] + "'s turn.")
                                        print(display_word)
                                        print("\n")
                                else:
                                    is_guessed = False

                        else:
                            playerIndex = (playerIndex + 1) % 3
                            print("Not a valid guess. It is now" + playerList[playerIndex] + "'s turn.")
                            print(display_word)
                            print("\n")
                    
                    else:
                        is_guessed = False

            else:
                playerIndex = (playerIndex + 1) % 3
                print("Not a valid guess. It is now" + playerList[playerIndex] + "'s turn.")
                print(display_word)
                print("\n")
    if is_guessed == True:
        print(playerList[playerIndex], "wins the round! $",players[playerIndex], "has been added to your bank.")
        banks[playerIndex] = players[playerIndex] 
        player1 = 0
        player2 = 0
        player3 = 0

def finalRound(word):
    max_bank = max(banks)
    max_index = banks.index(max_bank)
    print(playerList[max_index], "moves on to the final round.")
    display_word = "_" * len(word)
    is_guessed = False
    word_list = list(display_word)
    letter_position = [i for i, letter in enumerate(word) if letter == "R"]
    for index in letter_position:
        word_list[index] = "R"
    display_word = "".join(word_list)
    word_list = list(display_word)
    letter_position = [i for i, letter in enumerate(word) if letter == "S"]
    for index in letter_position:
        word_list[index] = "S"
    display_word = "".join(word_list)
    word_list = list(display_word)
    letter_position = [i for i, letter in enumerate(word) if letter == "T"]
    for index in letter_position:
        word_list[index] = "T"
    display_word = "".join(word_list)
    word_list = list(display_word)
    letter_position = [i for i, letter in enumerate(word) if letter == "L"]
    for index in letter_position:
        word_list[index] = "L"
    display_word = "".join(word_list)
    word_list = list(display_word)
    letter_position = [i for i, letter in enumerate(word) if letter == "N"]
    for index in letter_position:
        word_list[index] = "N"
    display_word = "".join(word_list)
    word_list = list(display_word)
    letter_position = [i for i, letter in enumerate(word) if letter == "E"]
    for index in letter_position:
        word_list[index] = "E"
    display_word = "".join(word_list)
    print(display_word)
    print("\n")
    print("For the final round, please guess 3 consonants and 1 vowel. The letters R,S,T,L,N,E have already been guessed.")
    while is_guessed == False:
        guess1 = input("Please guess your first consonant: ").upper()
        if len(guess1) == 1 and guess1 in consonant_list:
            guess2 = input("Please guess your second consonant: ").upper()
            if len(guess2) == 1 and guess2 in consonant_list:
                guess3 = input("Please guess your third consonant: ").upper()
                if len(guess3) == 1 and guess3 in consonant_list:
                    guessV = input("Please guess your vowel: ").upper()
                    if len(guessV) == 1 and guessV in vowel_list:
                        word_list = list(display_word)
                        letter_position = [i for i, letter in enumerate(word) if letter == guess1]
                        for index in letter_position:
                            word_list[index] = guess1
                        display_word = "".join(word_list)
                        word_list = list(display_word)
                        letter_position = [i for i, letter in enumerate(word) if letter == guess2]
                        for index in letter_position:
                            word_list[index] = guess2
                        display_word = "".join(word_list)
                        word_list = list(display_word)
                        letter_position = [i for i, letter in enumerate(word) if letter == guess3]
                        for index in letter_position:
                            word_list[index] = guess3
                        display_word = "".join(word_list)
                        word_list = list(display_word)
                        letter_position = [i for i, letter in enumerate(word) if letter == guessV]
                        for index in letter_position:
                            word_list[index] = guessV
                        display_word = "".join(word_list)
                        print(display_word)
                        print("\n")
                        final_guess = input("Please guess the word: ").upper()
                        if final_guess != word:
                            print("Sorry, that is incorrect. You did not win.")
                            break
                        else:
                            is_guessed = True
                            display_word = word

                        
                    else:
                        print("Not a valid guess.")

                else:
                    print("Not a valid guess.")

            else:
                print("Not a valid guess.")

        else:
            print("Not a valid guess.")
    if is_guessed == True:
        print("Congratulations! You won $",banks[max_index])
    







def main():
    word ="first".upper()
    firstRounds(word)
    word="second".upper()
    firstRounds(word)
    word = "grapefruit".upper()
    finalRound(word)

main()
            

        
        



 
    









    








