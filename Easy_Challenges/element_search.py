from random import randint

my_list = sorted([randint(1, 100) for a in range(1, 25)])
print(my_list)


def element_search(input_number):
    count = 0
    for item in my_list:
        if input_number in my_list:
            count += 1
            print("Number found in list %s times." % count)
            return True
        else:
            return False


print(element_search(int(input("Enter number to search: "))))


# Write a function that takes an ordered list of numbers (a list where the elements are in order
# from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and
# returns (then prints) an appropriate boolean.
#
# Extras: Use binary search.
