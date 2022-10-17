import string
from random import randrange


def input_pencils():
    global pencils, error_exist
    error_exist = True

    print("How many pencils would you like to use:")
    while error_exist:
        pencils = input()
        error_found = False

        for x in pencils:
            if x in string.ascii_letters:
                print("The number of pencils should be numeric")
                error_found = True
            elif x in string.punctuation:
                print("The number of pencils should be numeric")
                error_found = True

        if not error_found:
            if pencils == ' ':
                print("The number of pencils should be numeric")
            elif int(pencils) == 0:
                print("The number of pencils should be positive")
            elif int(pencils) < 0:
                print("The number of pencils should be numeric")
            else:
                error_exist = False


def set_players():
    players_not_set = True
    print("Who will be the first (John, Jack):")

    while players_not_set:
        global person

        person = input()
        if person == "Jack":
            players_not_set = False
        elif person == "John":
            players_not_set = False
        else:
            print("Choose between 'John' and 'Jack'")


def print_initial_pencils_and_turn():
    print(int(pencils) * "|")
    print("{}'s turn:".format(person))


def turn_and_print_player_pencils():
    global pencils, error_exist, remove_pencils
    error_exist = True

    while error_exist:
        remove_pencils = input()
        check_turn_errors()

    pencils = int(pencils) - int(remove_pencils)
    print(pencils * "|")


def check_turn_errors():
    global error_exist

    if remove_pencils in string.ascii_letters:
        print("Possible values: '1', '2' or '3'")
    elif remove_pencils in string.punctuation:
        print("Possible values: '1', '2' or '3'")
    elif len(remove_pencils) > 1:
        print("Possible values: '1', '2' or '3'")
    elif remove_pencils == ' ':
        print("Possible values: '1', '2' or '3'")
    elif int(remove_pencils) > 3:
        print("Possible values: '1', '2' or '3'")
    elif int(remove_pencils) <= 0:
        print("Possible values: '1', '2' or '3'")
    elif int(remove_pencils) > int(pencils):
        print("Too many pencils were taken")
    else:
        error_exist = False


def print_player_turn():
    global person

    if person == "Jack":
        person = "John"
    else:
        person = "Jack"

    if int(pencils) > 0:
        print("{}'s turn:".format(person))


def turn_and_print_bot_pencils():
    global pencils, error_exist, remove_pencils
    error_exist = True

    if pencils == 3:
        remove_pencils = 2
    elif pencils == 2:
        remove_pencils = 1
    elif pencils == 1:
        remove_pencils = 1
    elif int(pencils) % 4 == 0:
        remove_pencils = 3
    elif int(pencils) % 4 == 3:
        remove_pencils = 2
    elif int(pencils) % 4 == 2:
        remove_pencils = 1
    elif int(pencils) % 4 == 1:
        remove_pencils = 1
    else:
        remove_pencils = randrange(1, 4)

    print(remove_pencils)
    pencils = int(pencils) - int(remove_pencils)
    print(pencils * "|")


def declare_winner():
    if person == "Jack":
        print("Jack won!")
    else:
        print("John won!")


# Start of the program
input_pencils()
set_players()
print_initial_pencils_and_turn()

while int(pencils) > 0:
    if person == "John":
        turn_and_print_player_pencils()
        if pencils == 0:
            if person == "Jack":
                person = "John"
            else:
                person = "Jack"
            break
        print_player_turn()
    else:
        turn_and_print_bot_pencils()
        print_player_turn()

declare_winner()
