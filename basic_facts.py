# Main routine starts here
import math


def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that is"
                 f"between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check integer is not too low...
            if low is not None and response < low:
                print(error)

            # check the integer is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
                return response


        except ValueError:
            print(error)



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

equation_list = ["x", "-", "+", ]

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
    int_one = random.randint(1,9)
    int_two = random.randint(1,9)

    user_choice = int_check("Chose: ")



    # if the user input answer, display if they are either correct or wrong




    # if user choice is exit code, break the loop
    if user_choice == "xxx":
        break






