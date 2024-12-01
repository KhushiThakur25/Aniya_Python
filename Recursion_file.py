#Recursion : a function calls itself..

'''def info(n):
    if n < 1:
        return
    print("Hello user",n)
    info(n-1)
    print("Hello user",n)

info(5)'''

def fact(n,f):
    if n < 1:
        return f
    f *= n
    return fact(n-1,f)
result = fact(5,1)
print(result)
