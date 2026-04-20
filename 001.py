# print the stars =>
# *
# * *
# * * *
# * * * *

number = 1

while number < 5:
    i = 0
    while i < number:
        print("*", end=" ")
        i += 1

    number += 1
    print("")


# using for loop print same pattern

i = 1

while i < 5:
    for j in range(1, i + 1):
        print("*", end=" ")
    i += 1
    print()
