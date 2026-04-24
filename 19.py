# Practice Problem: Given a list of dictionaries (representing employees), sort them based on their “salary” in descending order using a lambda function.


employees = [
    {"name": "A", "salary": 50},
    {"name": "B", "salary": 70},
    {"name": "C", "salary": 60},
]

sorted_list = list(sorted(employees, key=lambda x: x["salary"], reverse=True))

print(sorted_list)
