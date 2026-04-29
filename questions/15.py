# Practice Problem: Given a list of strings, use a single list comprehension to extract strings that meet two criteria: they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).

str1 = ["apple", "education", "ice", "ocean", "python", "umbrella"]


result_str = [
    item
    for item in str1
    if len(item) > 5 and item[0].lower() in ["a", "e", "i", "o", "u"]
]
print(result_str)
