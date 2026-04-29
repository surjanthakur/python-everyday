# Practice Problem: Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive.

# from collections import Counter : # you can usr Counter it  automatically builds the frequency map.

text = "Python Programming"


def str_count(input_str: str):
    counter = {}
    for i in input_str:
        if i not in counter:
            counter[i] = input_str.count(i)
        continue
    print(counter)


str_count(input_str=text.lower().replace(" ", ""))
