#  Dictionary Merging with Logic =>

# Practice Problem: Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.


dict_a = {"a": 10, "b": 20}
dict_b = {"b": 5, "c": 15}


def merg_dict(dict1: dict, dict2: dict):
    result = dict1.copy()
    for key, val in dict2.items():
        result[key] = result.get(key, 0) + val

    print(result)


merg_dict(dict1=dict_a, dict2=dict_b)
