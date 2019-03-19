"""Quiz and answers about Apple"""
Apple_quiz = ("The most valuable company in terms of market cap in 2016 is, ___1___."
              "It was founded in ___2___. Its flagship product is called ___3___."
              "___1___ has many competitors, the biggest rival is ___4___,founded by"
              " nobody but the richest man on the planet,___5___ ___6___.")

list_of_answers_Apple = ["Apple", "1976", "Iphone", "Microsoft", "Bill", "Gates"]


"""Quiz and answers about Bond"""
Bond_quiz = ("James Bond is agent ___1___. He serves his country,___2___ ___3___"
             " against its enemies. His car of choice is usually ___4___ ___5___."
             "  His favorite drink is ___6___.")

list_of_answers_Bond = ["007", "United", "Kingdom", "Aston", "Martin", "Martini"]

"""Quiz and answers about programming basics"""
Programming_quiz =  ("___1___ are created with the def keyword. ___1___ are also called ___2___"
                   " You specify the inputs a ___1___ take by adding ___3___ separated by commas"
                   " between the parentheses. ___3___ can be standard data types such as string, number"
                   " ,dictionary, tuple, and ___4___ or can be more complicated such as ___5___"
                   " and ___6___ functions.")

list_of_answers_Programming = ["Functions", "procedures", "arguments", "lists", "objects", "lambda"]

blank_space = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___]"]


#List of levels with corresponding lives/guesses that player can have
quiz_list = ["Apple", "Bond", "Programming"]
level_list = ["easy", "medium", "hard", "superhard", "insane"]
lives_easy = 5
lives_medium = 4
lives_hard = 3
lives_superhard = 2
lives_insane = 1


def choose_quiz():
    """ Prompts player to pick a type of quiz and loads the quiz """
    #Input = player_quiz (raw input from player)
    #Output = loaded quiz, player chose
    while True:
        player_quiz = raw_input("Please, select a quiz you want to play: "
                          "(Apple, Bond or Programming): ")
        if player_quiz == "Apple":
            return Apple_quiz
        elif player_quiz == "Bond":
            return Bond_quiz
        elif player_quiz == "Programming":
            return Programming_quiz
        else:
            print "We don't have such quiz, pick again!"

def answers_for_quiz():
    """ Loads appropiate answers to the quiz that player has chosen"""
    #Input = player quiz (raw input from player)
    #Output = loaded quiz answers from the quiz player chose
    player_quiz_pick = choose_quiz()
    if player_quiz_pick == Apple_quiz:
        return list_of_answers_Apple
    elif player_quiz_pick == Bond_quiz:
        return list_of_answers_Bond
    elif player_quiz_pick == Programming_quiz:
        return list_of_answers_Programming

def player_level():
    """ Loads a difficulty that player chooses """
    #Input = player_level_input (raw input of player choosing a difficulty)
    #Output = corresponding number of lives:
    #Easy = 5 lives, Medium = 4 lives
    #Hard = 3 lives, Superhard = 2 lives
    #Insane = 1 life
    while True:
        player_level_input = raw_input("Please type in a difficulty level: "
                                 "(easy, medium, hard, superhard, insane): ")
        if player_level_input == "easy":
            return lives_easy #Easy = 5 lives
        elif player_level_input == "medium":
            return lives_medium #Medium = 4 lives
        elif player_level_input == "hard":
            return lives_hard #Hard = 3 lives
        elif player_level_input == "superhard":
            return lives_superhard #Superhard = 2 lives
        elif player_level_input == "insane":
            return lives_insane #Insane = 1 life
        else:
            print "We do not have such difficulty! Pick again!"

def correct_answer(player_answer, list_of_answers, answers_index):
    """ Checks, whether the the answer from player matches with the answer list. """
    #Input: player_answer (raw input that player enters in order to fill in the blank)
    #Output: "Right answer!" or "Wrong! Try again!" this output will be later used in the game
    if player_answer == list_of_answers[answers_index]:
        return "Right answer!"
    return "Wrong! Try again!"

def initialize_game():
    """Functions that sets up a game so we can play it """
    player_quiz_pick, player_level_pick, list_of_answers = choose_quiz(), player_level(), answers_for_quiz()
    print player_quiz_pick
    print "\nYou will get maximum " + str(player_level_pick) + " guesses for this game. Good luck.\n"
    blanks_index, answers_index, player_lives = 0, 0, 0

    #for elements in blank_space:
    while blanks_index < len(blank_space):
        player_answer = raw_input("Please type in your answer for " + blank_space[blanks_index] + ": ")
        if correct_answer(player_answer,list_of_answers,answers_index) == "Right answer!":
            print "Correct answer! Keep going!\n"
            player_quiz_pick = player_quiz_pick.replace(blank_space[blanks_index],player_answer)
            answers_index += 1
            blanks_index += 1
            print player_quiz_pick
            if blanks_index == len(blank_space):
                print "Congratulations! You nailed it! You are the winner!"
        else:
            player_level_pick -= 1
            if player_level_pick == 0:
                print "Game over! Maybe next time!"
                break
            else:
                print "One life less, that sucks! Have another shot!"
                print "You have " + str(player_level_pick) + " guesses left."

initialize_game()