import random
import re
import time


def hidelist(n):
    #Returns a hidden list, so the user wont know the letters.
    hidden_list = database[n][:]
    for i in range(len(hidden_list)):
        hidden_list[i] = re.sub('.', '_', hidden_list[i])
    return hidden_list


def input_check(letter):
    #Checks if the user input is legal. Also returns False if he re enters a letter.
    global all_guess
    pattern = "^[a-z]$"
    m = re.match(pattern, letter)
    if m:
        if letter in all_guess:
            print("You have already guessed this letter")
            return False
        else:
            all_guess = all_guess + letter
            return m
    print("You can only enter one letter from the ABC")
    return m


def guess(hidden_list, n):
    # The user will make his guesses, and will get his points rewarded
    global points
    while database[n] != hidden_list:
        print(hidden_list)
        letter = input("Please guess a letter ")
        letter = letter.lower()
        while not input_check(letter):
            letter = input("Please guess a letter ")
            letter = letter.lower()
        answer = False
        for i in range(len(database[n])):
            hidden_list[i] = list(hidden_list[i])
            for x in range(len(database[n][i])):
                if database[n][i][x] == letter:
                    answer = True
                    hidden_list[i][x] = letter
            hidden_list[i] = ''.join(hidden_list[i])
        if answer:
            points = points + 5
        else:
            points = points - 1


def game():
    # The game itself, will call to all the relevant functions.
    global points
    n = random.randint(0, 9)
    hidden_list = hidelist(n)
    start_time = time.time()
    guess(hidden_list, n)
    end_time = time.time()
    if (end_time - start_time) < 30:
        points = points + 30
    print("You got " + str(points) + " points!")

#Start of main code and database
all_guess = ""
points = 0
database = [['ace', 'from', 'space'], ['i', 'got', 'nuts'],
            ['zero', 'to', 'hero'], ['what', 'a', 'fold'],
            ['i', 'raise', 'pot'], ['steph', 'from', 'three'],
            ['ben', 'the', 'man'], ['i', 'am', 'bored'],
            ['check', 'the', 'news'], ['money', 'in', 'grave']]
game()
