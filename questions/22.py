# Practice Problem: Write a function that generates the Power Set of a given set (a set of all possible subsets, including the empty set and the set itself).

from itertools import combinations

input_list = {1, 2, 3}


def get_power_set(power_list: list):
    power_set = []
    elements = list(power_list)

    for i in range(len(elements) + 1):
        for comb in combinations(elements, i):
            power_set.append(comb)

    return power_set


ans = get_power_set(input_list)
print(ans)
