def deposit(balance):
    amount = float(input("balansni kiriting: "))
    if amount > 0:
        resalt = balance + amount
        print(f"pul qoshildi {resalt:,.2f}")
def withdraw(balance):
    amount = float(input("yechish balansni kiriting: "))
    if amount < balance:
        resalt = balance - amount
        print(f"pul yechib olindi qolgan balans {resalt:,.2f}")
    else:
        print("mablag' yetarli emas")
def check_balance(balance):
    print(f"hozirgi balans {balance:,.2f}")
def main():
    balance = 100000
    print("""
          1: deposit,
          2: withdraw,
          3: check balance
          """)
    amal = int(input("amalni tanlang: "))
    if amal == 1:
        deposit(balance)
    elif amal == 2:
        withdraw(balance)
    elif amal == 3:
        check_balance(balance)
    else:
        print("bunday amal mavjud emas")

main()
