# Practice Problem: Merge two dictionaries. If they share a key, the new dictionary should store a list containing values from both dictionaries instead of overwriting the first one.


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}


def merge_dict(dict1: dict, dict2: dict) -> dict:
    new_dict = {}
    all_keys = set(dict1.keys()) | set(dict2.keys())
    for key in all_keys:
        values = []
        if key in dict1:
            values.append(dict1[key])
        if key in dict2:
            values.append(dict2[key])
        new_dict[key] = values

    return new_dict


ans = merge_dict(d1, d2)

print(ans)
