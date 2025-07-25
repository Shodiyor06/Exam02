students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
]
names = list(map(lambda x: x.get("name"),students))
len_names = list(map(lambda y: len(y),names))
min_name = min(len_names)
name = ""
for i in names:
    if len(i) == min_name:
        print(i)
