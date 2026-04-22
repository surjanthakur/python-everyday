# Practice Problem: Create a function rotate_list(lst, n, direction) that shifts the elements of a list by N positions. The direction can be ‘left’ or ‘right’.


def rotate_list(inp_list: list, num: int, direction: str = "right") -> list:
    if not inp_list:
        return inp_list

    n = num % len(inp_list)

    if direction == "right":
        return inp_list[n + 1 :] + inp_list[: n + 1]
    else:
        return inp_list[n:] + inp_list[:n]


data = [1, 2, 3, 4, 5]
ans = rotate_list(data, 2, "right")

print(ans)
