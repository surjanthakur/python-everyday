# Practice Problem: Create a function that “inverts” a dictionary. Convert a dictionary of Author: [List of Books] into a dictionary of Book: Author.


input_dict = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}


def inverts_dict(inp_dict: dict):
    new_dict = {}
    for i in inp_dict:
        for j in inp_dict[i]:
            new_dict[j] = i
    return new_dict


ans = inverts_dict(input_dict)
print(ans)
