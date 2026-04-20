# Print list in reverse order using a loop =>
# Practice Problem: Given a list, iterate it in reverse order and print each element.
# Exercise Purpose: Learning to Traverse Data Backwards is essential for many data structures. This exercise shows how to use the reversed() function or custom range slicing to iterate over a list from the end to the beginning.


list1 = [10, 20, 30, 40, 50]
rev_list = []


for i in reversed(list1):
    rev_list.append(i)

print(rev_list)
