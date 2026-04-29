# Practice Problem: Given two lists of student IDs, find the IDs that appear in either the first or the second list, but not in both.


list1 = [101, 102, 103]
list2 = [103, 104, 105]

new_list = []

for i in list1:
    if i in list2:
        list1.remove(i)
        list2.remove(i)

new_list.extend(list1)
new_list.extend(list2)

print(new_list)
