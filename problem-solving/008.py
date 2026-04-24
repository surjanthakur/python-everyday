# Practice Problem: Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).


word1 = "listen"
word2 = "silent"


def is_anagrams(str1: str, str2: str):
    s1 = sorted(str1.lower().replace(" ", ""))
    s2 = sorted(str2.lower().replace(" ", ""))

    return s1 == s2


print(is_anagrams(str1=word1, str2=word2))
