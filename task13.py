import json

with open('Input/students.json', 'r') as file:
    data = json.load(file)

names = [student['name'] for student in data]
lst = []
for i in names:
    if len(i) > 5:
        lst.append(i)
output = {"long_names": lst}

with open('Output/output13.json', 'w') as file:
    json_str = json.dumps(output, indent=4)
    file.write(json_str)