# Practice Problem: Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements.


def sort_list(input_list: list):
    result = []

    for i in input_list:
        if isinstance(i, list):
            result.extend(sort_list(input_list=i))
        else:
            result.append(i)

    return result


nested = [1, [2, 3], [4, [5, 6]], 7]
sort = sort_list(nested)

print(sort)
