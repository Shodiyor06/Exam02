import json

with open('Input/students.json', 'r') as file:
    content = file.read()
    data = json.loads(content)
    t_soni = 0
    for i in data:
        t_soni += 1
with open('Output/output11.json', 'w') as file:
    json_str = json.dumps(t_soni, indent=4)
    file.write(json_str)