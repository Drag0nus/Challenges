result = []


def remove_duplicates(input_list):
    for i in input_list:
        if i in input_list and i not in result:
            result.append(i)
    return result


def sets_example(input_list):
    set_result = set()
    for i in input_list:
        set_result.add(i)
    return set_result

print(remove_duplicates([1001, 1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 7, 10, 10, 100, 100, 1001]))
print(sets_example([1001, 1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 7, 10, 10, 100, 100, 1001]))

# Write a program (function!) that takes a list and returns a new list that contains all the
# elements of the first list minus all the duplicates.
#
# Extras:
#
#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.
