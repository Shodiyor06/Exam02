import json

with open('Input/students.json', 'r') as file:
    data = json.load(file)

names = [student['name'] for student in data]
lst = []
for i in names:
    if i[0] == 'A':
        lst.append(i)
output = { "a_names": lst}

with open('Output/output14.json', 'w') as file:
    json_str = json.dumps(output, indent=4)
    file.write(json_str)