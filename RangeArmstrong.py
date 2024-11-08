import math

for n in range(1,1001):
    org = n
    count = 0
    sum = 0
    while n > 0:
        count += 1
        n //= 10

    n = org
    while n > 0:
        sum += pow(n%10,count)
        n //= 10

    if org == sum:
        print(org)
