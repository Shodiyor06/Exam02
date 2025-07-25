students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}
ball = 0
for i in students.values():
    ball += i
avg = ball / len(students)
lst = []
for key, value in students.items():
    if value > avg:
        lst.append(key)
print(f"{avg} dan baland ball olganlar {lst}")