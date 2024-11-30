Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(a,b):
...     print(a,b)
... 
>>> add(3,5)
3 5
>>> def add(a,b):
...     print(b,a)
... 
>>> add(3,5)
5 3
>>> add(5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    add(5)
TypeError: add() missing 1 required positional argument: 'b'
>>> def add(a,b):
...     print(a,b)
... 
add(b = 5,a = 6)
6 5
add(x= 5,y = 3)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    add(x= 5,y = 3)
TypeError: add() got an unexpected keyword argument 'x'
add(2)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    add(2)
TypeError: add() missing 1 required positional argument: 'b'
def add(a = 5,b = 6,c = 4):
    print(a,b,c)

add()
5 6 4
add(5,2)
5 2 4
def add(args*):
    
SyntaxError: invalid syntax
def add(args*):
    
SyntaxError: invalid syntax
def add(*args):
    print(args)

add(5,2,63,4,6,8)
(5, 2, 63, 4, 6, 8)
def add(**kwargs):
    print(kwargs)

add(a = 56, b = 32, c = 95)
{'a': 56, 'b': 32, 'c': 95}
eval("32*56/41+95-74")
64.70731707317074
exec('arr=5')
arr
5
exec('b = 32*56/41+95-74')
b
64.70731707317074
exec('32*56/41+95-74')
temp = [223,54,67,99,75,17,25,35,65,965]
def c_to_f(c):
    return 9/5*c+32

f=[]
for i in temp:
    f.append(c_to_f(i))

f
[433.40000000000003, 129.2, 152.60000000000002, 210.20000000000002, 167.0, 62.6, 77.0, 95.0, 149.0, 1769.0]
map(c_to_f,temp)
<map object at 0x0000024CA403BEB0>
list(map(c_to_f,temp))
[433.40000000000003, 129.2, 152.60000000000002, 210.20000000000002, 167.0, 62.6, 77.0, 95.0, 149.0, 1769.0]
def even(i):
    return i%2 == 0

def odd(i):
    return i%2 != 0

e =[]
o =[]
for i in temp:
    if even(i):
        e.append(i)
    elif odd(i):
        o.append(i)

e
[54]
o
[223, 67, 99, 75, 17, 25, 35, 65, 965]
list(filter(even,temp))
[54]
list(filter(odd,temp))
[223, 67, 99, 75, 17, 25, 35, 65, 965]
def cube(y):
    return y*y*y

lambda_cube = lambda y:y*y*y
cube(5)
125
lambda_cube(5)
125
lambda_val = [lambda x=i:x*10 for i in range(1,5)]
for i in lambda_val:
    print(i())

10
20
30
40
