from random import *

a = [1, 1, 2, 3, 5, 13, 21, 34, 55, 89, 100, 110, 12312431, 123, 2342, 24, 234]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 34, 55, 234]
generated_list1 = []
generated_list2 = []

for i in range(0, int(random() * 100)):
    generated_list1.append(int(random() * 100))

for i in range(0, int(random() * 100)):
    generated_list2.append(int(random() * 100))

print(generated_list1)
print(generated_list2)


def overlap(list_1, list_2):
    result = []
    if len(list_1) > len(list_2):
        for item in range(0, len(list_1)):
            if list_1[item] in list_2 and list_1[item] not in result:
                result.append(list_1[item])
    else:
        for item in range(0, len(list_2)):
            if list_2[item] in list_1 and list_2[item] not in result:
                result.append(list_2[item])
    return result


print("overlap a and b - ", overlap(a, b))
print("overlap gen_list1 and gen_list2 - ", overlap(generated_list1, generated_list2))


# Take two lists, say for example these two:
# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
# Extras:
#
#     Randomly generate two lists to test this

#     Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
