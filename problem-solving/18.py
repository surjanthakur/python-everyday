# Practice Problem: Merge two dictionaries. If they share a key, the new dictionary should store a list containing values from both dictionaries instead of overwriting the first one.


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}


def merge_dict(d1: dict, d2: dict):
    all_keys = set(d1.keys) | set(d2.keys)
