numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]
daraja = list(map(lambda x: x['value'] ** 2, numbers))
print(daraja)
