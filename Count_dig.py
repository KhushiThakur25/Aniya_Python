n = int(input("Enter the number"))
count = 0
while n != 0:
    count += 1
    n //= 10
print(f"Your count of digit is {count}")