# Holds all functions for the Hangman game in the file Hangman_Code.
import Random_Words
import random
import turtle

def get_word(difficulty):
    """Gets a randomly selected word from Random_Words file."""
    if difficulty == "easy":
        word = Random_Words.word_list_easy[random.randint(0,(len(Random_Words.word_list_easy) - 1))]
    elif difficulty == "medium":
        word = Random_Words.word_list_medium[random.randint(0,(len(Random_Words.word_list_medium) - 1))]
    elif difficulty == "hard":
        word = Random_Words.word_list_hard[random.randint(0,(len(Random_Words.word_list_hard) - 1))]
    elif difficulty == "nightmare":
        word = Random_Words.word_List_nightmare[random.randint(0,(len(Random_Words.word_List_nightmare) - 1))]

    return word
    

def hide_letters(word):
    """Turns the letters of chosen word into underscores and spaces in between the letters."""
    for letter in range(0, len(word)):
        list_word = list(word)
        list_word[letter] = "_"
        word = list_word
        
    return " ".join(list_word)
        

def play_round(word, guess):
    """Begins a new round in a game of Hangman."""
    guess_right = False
    if guess in word:
        guess_right = True

    return guess_right


def show_letter(player_guess, placeholder, word):
    """If the player guesses a correct letter, then the correct letter will appear in its correct position in the word."""
    # Sets the max amount of the range for the for loop below.
    letter_count = len(placeholder)
    
    # Seperates placeholder into individual values.
    placeholder = list(placeholder)
    
    for index in range(0, letter_count):

        # Alters word into the same format as placeholder
        word_listed = " ".join(list(word))
        word_listed = list(word_listed)

        # Checks if the player's guess is in the chosen word, and if it is, the letter is revealed to the player.
        if player_guess == word_listed[index]:
            placeholder[index] = player_guess
            
    # Returns placeholder into its original format.
    placeholder = "".join(placeholder)

    return placeholder


def letter_guessed(player_guess, list_of_guesses):
    """When a player guesses a letter, the letter is added to a list of previously guessed letters."""
    return list_of_guesses.append(player_guess)


def did_player_win(word, placeholder):
    """Checks if the player has guessed correctly all the letters in the chosen word."""
    # Alters word to match the style of placeholder.
    word = " ".join(list(word))

    return word == placeholder
    

def display_game_info(lives, list_of_guesses, hidden_word):
    """Displays important game info such as current amount of lives, guessed letters, and the outline of the word."""
    print("ROUND INFO: ")
    print(f"Your remaining lives: {lives}")
    print(f"Your hidden word is currently: {hidden_word}")
    print(f"You have guessed the following letters: {list_of_guesses}")
    print("")

def draw_hangman(lives):
    """Draws the Hangman Game the user is playing."""

    # Creates Turtle screen.
    screen = turtle.Screen()

    # Create a Turtle object
    t = turtle.Turtle()

    #Set the speed of the turtle
    t.speed(2)
    t.color()

    # Sets up the initial Hangman Game Drawing.
    t.penup()
    t.setheading(270)
    t.forward(200)
    t.pendown()
    t.left(90)
    t.forward(-100)
    t.left(90)
    t.forward(450)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(40)
    

    # 1 - Adds head to drawing.
    t.left(90)
    t.circle(-30)
    

    # 2 - Adds body to drawing.
    t.right(90)
    t.penup()
    t.forward(60)
    t.pendown()
    t.forward(125)


    # 3 - Adds first arm to drawing.
    t.left(180)
    t.penup()
    t.forward(80)
    t.pendown()
    t.right(50)
    t.forward(50)


    # 4 - Adds second arm to drawing.
    t.penup()
    t.forward(-50)
    t.pendown()
    t.left(100)
    t.forward(50)


    # 5 - Adds first leg to drawing.
    t.penup()
    t.forward(-50)
    t.right(50)
    t.forward(-80)
    t.left(230)
    t.pendown()
    t.forward(50)


    # 6 - Adds second leg to drawing.
    t.penup()
    t.forward(-50)
    t.right(100)
    t.pendown()
    t.forward(50)
    turtle.done()

