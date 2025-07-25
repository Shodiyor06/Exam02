import csv
with open("Input/grades.csv")  as file:
    content = list(csv.reader(file))
content = content[1:]
counter = 0
for i in content:
    if i[1] == '5':
        counter += 1 
with open("Output/output16.txt",'a') as f:
    f.write(f"5 baho olganlar soni:  {counter}")
