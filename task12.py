import json

with open('Input/students.json', 'r') as file:
    data = json.load(file)

names = [student['name'] for student in data]

sorted_names = sorted(names)

output = {"sorted_names": sorted_names}
with open('Output/output12.json', 'w') as file:
    json_str = json.dumps(output, indent=4)
    file.write(json_str)
