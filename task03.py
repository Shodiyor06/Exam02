def calculate_tax(salary):
    if salary > 5000000:
        tax = salary * 0.20
    else:
        tax = salary * 0.13
    return int(tax)

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    net_salary = salary - tax
    return int(net_salary)

salary = float(input("maoshni kiriting: "))
print("Soliq:", calculate_tax(salary))
print("Sof maosh:", calculate_net_salary(salary))
