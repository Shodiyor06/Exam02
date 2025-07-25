def add(a, b):
    resalt = a + b
    print(resalt)
def subtract(a, b):
    resalt = a - b
    print(resalt)
def multiply(a, b):
    resalt = a * b
    print(resalt)
def divide(a, b):
    resalt = a / b
    print(resalt)

def main():
    a = float(input("1 - sonni kiriting: "))
    b = float(input("2 - sonni kiriting"))
    amal = input("amal kiriting: ")
    if amal == '+':
        add(a, b)
    elif amal == '-':
        subtract(a, b)
    elif amal == '*':
        multiply(a, b)
    elif amal == '/':
        divide(a, b)
    else:
        print("bunday amal mavjud emas")
main()