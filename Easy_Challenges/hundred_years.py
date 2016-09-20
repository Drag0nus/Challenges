from datetime import *

current_year = datetime.now().year


def check_info():
    input_name = input("What's your name?\n")
    input_age = input("How old are you?\n")

    if len(input_name) and len(input_age) != 0:
        print("Hello,", input_name, ". You're", input_age, "years old.")
        print(input_name, ", You'll have ur 100th birthday in", (int(current_year) - int(input_age) + 100))
    else:
        print("Oops, you haven't enter some info. Try again.")
        check_info()


check_info()


# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras: Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)
