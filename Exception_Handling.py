'''x = 5
y = "hello"
try:
    z = x / 0
except Exception as msg:
    print(msg)'''



try:
    def add(a,b):
        print(f"Sum of {a} and {b} is {a+b}")
    def sub(a,b):
        print(f"Sub of {a} and {b} is {a-b}")
    def mul(a,b):
        print(f"mul of {a} and {b} is {a*b}")
    def div(a,b):
        print(f"div of {a} and {b} is {a/b}")
    
    a = int(input("Enter the value of a.."))
    b = int(input("Enter the value of b.."))
    add(a,b)
    sub(a,b)
    mul(a,b)
    div(a,b)
    
    
except ZeroDivisionError as msg:
    print(msg)
except TypeError as msg:
    print(msg)
except Exception as msg:
    print(msg)
finally:
    print("This is my app..")
    
    

    
