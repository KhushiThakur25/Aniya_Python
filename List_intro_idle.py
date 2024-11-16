Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = [1,2,3,4,5,6]
>>> len(li)
6
>>> li.append(65)
>>> li
[1, 2, 3, 4, 5, 6, 65]
>>> li.insert(3,100)
>>> li
[1, 2, 3, 100, 4, 5, 6, 65]
>>> li.append(2,3,56,4)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    li.append(2,3,56,4)
TypeError: list.append() takes exactly one argument (4 given)
>>> li.append([1,2,45,6])
>>> li
[1, 2, 3, 100, 4, 5, 6, 65, [1, 2, 45, 6]]
>>> li[8][2]
45
li.extend([1, 2, 45, 6])
li
[1, 2, 3, 100, 4, 5, 6, 65, [1, 2, 45, 6], 1, 2, 45, 6]
li.count(1)
2
li.pop()
6
li
[1, 2, 3, 100, 4, 5, 6, 65, [1, 2, 45, 6], 1, 2, 45]
remove(8)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    remove(8)
NameError: name 'remove' is not defined
li.remove(8)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    li.remove(8)
ValueError: list.remove(x): x not in list
li.remove([1, 2, 45, 6])
li
[1, 2, 3, 100, 4, 5, 6, 65, 1, 2, 45]
price = [200,510,2300,4562,988,799]
temp = price
temp
[200, 510, 2300, 4562, 988, 799]
for i in range(len(temp)):
    temp[i] = temp[i] - (0.15 * temp[i])

temp
[170.0, 433.5, 1955.0, 3877.7, 839.8, 679.15]
price
[170.0, 433.5, 1955.0, 3877.7, 839.8, 679.15]
price = [200,510,2300,4562,988,799]
temp = price.copy()
temp
[200, 510, 2300, 4562, 988, 799]
for i in range(len(temp)):
    temp[i] = temp[i] - (0.15 * temp[i])

temp
[170.0, 433.5, 1955.0, 3877.7, 839.8, 679.15]
price
[200, 510, 2300, 4562, 988, 799]
price.index(500)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    price.index(500)
ValueError: 500 is not in list
price.index(200)
0
price.clear()
price
[]
price = [200,510,2300,4562,988,799]
price.reverse()
price
[799, 988, 4562, 2300, 510, 200]
price.sort()
price
[200, 510, 799, 988, 2300, 4562]
price.sort(reverse = True)
price
[4562, 2300, 988, 799, 510, 200]
price.min()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    price.min()
AttributeError: 'list' object has no attribute 'min'
min(price)
200
max(price)
4562
sum(price)
9359
li = [10,50,100,60,150,80]
maxs = 0
sec = 0
for i in li:
    if i > maxs:
        sec = maxs
        maxs = i

print(maxs)
150
sec
100
li = [10,50,100,60,150,120]
maxs = 0
sec = 0
for i in li:
    if i > maxs:
        sec = maxs
        maxs = i

maxs
150
sec
100
maxs = 0
sec = 0
for i in li:
    if i > maxs:
        sec = maxs
        maxs = i
    if i < maxs and i > sec:
        sec = i

sec
120
maxs
150
