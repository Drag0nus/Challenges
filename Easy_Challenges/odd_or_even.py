number = int(input("Please enter some number: "))
check = int(input("And check number:"))
print("Your number and check are:", number, "and", check)

if number % 2 == 0:
    print("It's even.")
    if number % 4 == 0:
        print("It is a multiple of 4.")
else:
    print("It's odd.")

print("EXTRAS")

if number % check == 0:
    print("Check divides evenly into num.")
else:
    print("Check doesn't")

# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
#     If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
