#  Print elements from a list present at odd index positions
# Practice Problem: Given a Python list, use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.).

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

odd_list = []

for idx, val in enumerate(my_list):
    if idx % 2 == 1:
        odd_list.append(val)
    continue

print(odd_list)
