# Main routine starts here
# import math


def int_check(question):
    """Checks for an integer more than zero / <enter> for infinite"""
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)
            # check that the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


def math_compare(user, answer):

    # if the answer and the users choice is the same, the user is correct
    if user == answer:
        "correct"

    else:
        "incorrect"

def string_checker(question, valid_ans=('yes', 'no')):
    """Checks users enter and answer from a list"""

    error = f"please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does enter something that is valid
        print(error)
        print()

print()
print("✖️➕➗➖Basic Facts Math✖️➕➗➖")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("Do you want to see the instructions?")

print()

# display the instructions if user wants to see them
if want_instructions == "yes":
    print('''
        ***   Instructions   ***

    To begin, you have to pick how many games you want to play for.
    After you chosen how much games you picked, you then answer the question the computer ask.

    Good Luck!

    ''')

# game loop stats here

equation_list = ["*", "+", ]
game_history = []

import random

# initialise game variables
mode = "regular"
rounds_played = 0

num_rounds = int_check("How many rounds would you like?")
print()
print(f"you chose: {num_rounds}")


# game loop stats here
while rounds_played < num_rounds:

    # Rounds heading

    rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)
    print()

    rounds_played += 1

    # display the question for the user
    print("What is:")
    int_one = random.randint(1,12)
    equation_sym = random.choice (equation_list)
    int_two = random.randint(1,12)

    user_answer = int_check(f"{int_one} {equation_sym} {int_two} = ")
    answer = eval(f"{int_one} {equation_sym} {int_two} ")

    if user_answer == answer:
        feedback = "is correct"
    else:
        feedback = f"incorrect, the answer was {answer}"

    round_feedback = f"{feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

# game loop ends here

# display stats
see_history = string_checker("\nDo you want to see your game history")
if see_history == "yes":
    for item in game_history:
        print(item)

print()
print("Thank you for playing!")






























