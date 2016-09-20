from random import *

password = ""

easy_passwords = ["password", "qwerty", "football", "monkey11", "letmein5", "mustang95", "access", "schoolmaster"]
lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = lower_letters.upper()
symbols = " ~`!@#$%^&*()_+-=/']}?><"
numbers = "1234567890"

strength = input("Choose strength of your password (easy/medium/hard) or type 'exit' for exit program: ")


while strength != 'exit':
    if strength == "easy":
        password = easy_passwords[randint(0, len(easy_passwords) - 1)]
        break
    i = int(input("How long your password should be?"))
    if strength == "medium":
        while len(password) < i:
            password += lower_letters[randint(0, len(lower_letters) - 1)]
            password += upper_letters[randint(0, len(upper_letters) - 1)]
        break
    elif strength == "hard":
        while len(password) < i:
            password += lower_letters[randint(0, len(lower_letters) - 1)]
            password += upper_letters[randint(0, len(upper_letters) - 1)]
            # password += symbols[randint(0, len(symbols) - 1)]
        break
    if strength == 'exit':
        break
    else:
        print("Try again!")

print(password)


# Write a password generator in Python. Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
#
# Extra:
#
#     Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
