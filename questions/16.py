# Practice Problem: Write a function that removes duplicate elements from a list. You cannot use set() because sets do not maintain the original order of elements.

str_input = [1, 2, 2, 3, 1, 4, 2]


def rm_duplicate(input_list: list) -> list:
    unique_list = []
    for i in input_list:
        if i not in unique_list:
            unique_list.append(i)
        else:
            continue

    return unique_list


ans = rm_duplicate(input_list=str_input)

print(ans)
