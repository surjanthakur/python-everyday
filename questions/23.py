# Problem:
# Given a string s, find the length of the longest substring without repeating characters.

# exp:
# Input: "abcabcbb"
# Output: 3  # "abc"

s = "longpolling"


def long_sub(inp_str: str):
    long_substring = []
    for i in inp_str:
        if i not in long_substring:
            long_substring.append(i)

        if i in long_substring:
            break

    return "".join(long_substring)


ans = long_sub(inp_str=s)
print(ans)
