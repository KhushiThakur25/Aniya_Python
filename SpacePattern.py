# row = 5
# for i in range(row):
#     for j in range(row-1 - i):
#         print(" ",end = " ")
#     for k in range(row - i - 1 , row):
#         print("*",end = " ")
#     print()

# row = 5
# for i in range(row):
#     for j in range(0,i):
#         print(" ",end = " ")
#     for k in range(i,row):
#         print("*", end = " ")
#     print()

row = 4
for i in range(row):
    for j in range(0,row-i-1):
        print("+",end = " ")
    for k in range(2*i + 1):
        print("*", end = " ")
    print()