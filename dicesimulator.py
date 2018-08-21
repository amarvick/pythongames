"""
Game Project - Alex Marvick (August 20, 2018)
Description: Small beginner project to gain familiarity with Python Syntax
"""
import random
game_selection = True

############

def dice_simulator():
    game_playing = True
    while (game_playing):
        print("Do you want to roll the dice? Y/N")
        response = input().upper()
        if (response == 'N'):
            game_playing = False
            print("Thanks for playing!")
        elif (response == 'Y'):
            print("Rolling dice...")
            x = random.randint(1, 6)
            print("You rolled a: " + str(x));
        else:
            print("Please select 'Y' or 'N'.")
            
###########

def guess_the_number():
    game_playing = True
    computer_number = random.randint(1, 100)
    no_guesses = 1
    while (game_playing):
        print("I'm thinking of a number between 1 - 100. Can you guess?")
        your_guess = int(input())
        # if(isinstance(your_guess, int)): AM - TO HANDLE LATER
        if(your_guess > 100 or your_guess < 1):
            print("Please guess a number between 1 and 100...")
        elif(your_guess != computer_number):
            if (your_guess < computer_number):
                print("You're a little low...")
            else:
                print("You're a little high!")
            no_guesses += 1
        else:
            print("You guessed correctly! Congratulations!")
            print("It took you " + str(no_guesses) + " times to guess correctly.")
            game_playing = False
        #else:
        #   print("Integers only!")

##########

while(game_selection):
    print("HELLO! Which game interests you?\n1 Dice Simulator\n2 Guess the Number")
    response = input()
    if (response == "1"):
        dice_simulator()
        game_selection = False
    elif (response == "2"):
        guess_the_number()
        game_selection = False
    else:
        print("Please put in a number between 1 and 2.")
