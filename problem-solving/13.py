# Practice Problem: Write a recursive function to calculate the factorial of a non-negative integer.

number = 5


def cal_factorial(num: int) -> int:
    if num > 0:
        return num * cal_factorial(num - 1)
    else:
        return 1


factorial = cal_factorial(number)
print(f"factorial of {number} is : {factorial}")
