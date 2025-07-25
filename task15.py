import csv
with open("Input/grades.csv")  as file:
    content = list(csv.reader(file))
content = content[1:]
baho = []
for i in content:
    if i[1] == '5':
        baho.append(i)
        
with open("Output/output15.txt",'a') as f:
    f.write(f"bahosi eng yuqori uqivchi:  {baho}")
