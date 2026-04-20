# Practice Problem: Given a sentence, reverse each individual word within the string while maintaining the original word order.


string = "Python is awesome"
str2 = string.split(" ")
new_str = []

for item in str2:
    new_str.append(item[::-1])

print(" ".join(new_str))
