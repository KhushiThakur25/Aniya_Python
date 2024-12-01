def atm():
    total = 10000
    pin = input("Enter your PIN")
    if pin == "1234":
        print("Login Successfully..")
    else:
        raise ValueError("Login Failed ! Your Pin is INVALID, please try again..")
    amount = int(input("Enter the amount.."))
    if amount > total:
        raise ValueError("Your balance is insufficient..")
    else:
        total -= amount
        print("Your remaining balance is:",total)

try:
    atm()
except ValueError as msg:
    print(msg)
except Exception as msg:
    print(msg)
