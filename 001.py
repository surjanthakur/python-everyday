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
