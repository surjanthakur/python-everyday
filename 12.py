# Practice Problem: Write a recursive function addition() that calculates the sum of numbers from 0 to 10. A recursive function is a function that calls itself to solve smaller instances of the same problem.


num = 10


def addition(n1: int) -> int:
    if n1 > 0:
        return n1 + addition(n1 - 1)
    else:
        return 0


sum = addition(num)
print(sum)
