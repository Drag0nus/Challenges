number = int(input("Enter number: "))
result = []


def Fibonacci(input_int):
    for i in range(0, input_int):
        if i == 0:
            result.append(1)
        if i == 1:
            result.append(1)
        if i > 1:
            result.append(result[i - 1] + result[i - 2])
    return result

print(Fibonacci(number))

# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
#
# (Hint: The Fibonnaci sequence is a sequence of numbers where the next number in the sequence is
# the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
