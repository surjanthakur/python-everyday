# Practice Problem: Create an outer function that accepts two parameters, a and b. Inside, create an inner function that calculates the addition of a and b. The outer function should then add 5 to that sum and return the final result.


def outer(n1, n2):
    def inner(a, b):
        return a + b

    result = inner(n1, n2)
    return result + 5


num = outer(12, 34)

print(num)
