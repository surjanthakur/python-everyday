# Practice Problem: Write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks.

string = "A man, a plan, a canal: Panama"


def palindrome(inp_str: str) -> bool:
    clear_char = [x.lower() for x in inp_str if x.isalnum()]
    clean_str = "".join(clear_char)
    return clean_str == clean_str[::-1]


ans = palindrome(string)
print(ans)
