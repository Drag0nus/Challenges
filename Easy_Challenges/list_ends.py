def list_ends(input_list):
    result = [i for i in input_list if i == input_list[0] or i == input_list[len(input_list)] - 1]
    return result


a = [1, 5, 10, 15, 20, 25, 200]
print(list_ends(a))


# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.
