def yes_no(question):
    """Checks user response to a question is yes ? no (y/n), returns 'yes or 'no"""

    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("pick yes / no please")


def instructions():
    """Prints instructions"""

    print("""
