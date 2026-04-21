# Practice Problem: Create a function that takes a list of numbers as input and returns the largest item from that list without using the built-in max() function (to practice manual logic).

nums = [1, 2, 3, 4, 5, 67, 45, 67, 23, 78, 45]


def big_num(nums: list):
    max_num = 0
    for i in nums:
        if i > max_num:
            max_num = i
    print(max_num)


big_num(nums)
