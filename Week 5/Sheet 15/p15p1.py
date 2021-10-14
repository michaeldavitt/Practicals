"""
Pseudo Code:

Define a recursive function with one formal parameter n:
    if n is equal to 1:
        return 2

    else:
        return n + f(n - 1)

Prompt the user for an integer

while the user integer is greater than or equal to 1:
    Read the integer

    for each number i in the range 0 to user integer - 1:
        print the result of the call to the recursive function with argument i + 1

Terminate the program
"""

def series_fn(n):
    print("Current number:", n)

    if n == 1:
        return 2

    else:
        return n + series_fn(n - 1)

user_num = int(input("Please enter an integer >= 1 (enter a non-positive number to exit): "))

while user_num >= 1:
    print("You have entered:", user_num)

    for i in range(user_num):
        print(series_fn(i + 1))

    user_num = int(input("Please enter an integer >= 1 (enter a non-positive number to exit): "))
    
print("Finished!")