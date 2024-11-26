Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[7,4,1],[8,5,2],[9,6,3]]
for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j] = a[i][j] + b[i][j]

a
[[8, 6, 4], [12, 10, 8], [16, 14, 12]]
#tuple - immutable
tu = 1,23,45,65,7
type(tu)
<class 'tuple'>
tup = (12,45,68,61,6)
type(tup)
<class 'tuple'>
tu[3]
65
tu.count(23)
1
len(tu)
5
del tu
tu
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tu
NameError: name 'tu' is not defined
sum(tup)
192
max(tup)
68
min(tup)
6
tup.index(68)
2
tup[2] = 100
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    tup[2] = 100
TypeError: 'tuple' object does not support item assignment
#modify tuple using type conversion of data structure
tup = list(tup)
tup
[12, 45, 68, 61, 6]
tup[2] = 100
tup
[12, 45, 100, 61, 6]
tup = tuple(tup)
tup
(12, 45, 100, 61, 6)
s={}
type(s)
<class 'dict'>
s1 = {1,2,3,4,5,6}
s2 = {4,6,8,9}
s1.union(s2)
{1, 2, 3, 4, 5, 6, 8, 9}
s = {1,1,2,1,2,45,12,1,2}
s
{1, 2, 12, 45}
s[1]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable
s1
{1, 2, 3, 4, 5, 6}
s2
{8, 9, 4, 6}
s1.update(s2)
s1
{1, 2, 3, 4, 5, 6, 8, 9}
s1 = {1,2,3,4,5,6}
s1.interection(s2)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s1.interection(s2)
AttributeError: 'set' object has no attribute 'interection'. Did you mean: 'intersection'?
s1.intesection(s2)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s1.intesection(s2)
AttributeError: 'set' object has no attribute 'intesection'. Did you mean: 'intersection'?
s1.intersection(s2)
{4, 6}
s1.intersection_update(s2)
s1
{4, 6}
s1 = {1,2,3,4,5,6}
s2 = {4,6,8,9}
s3 = {1,2,3}
s1.issuperset(s3)
True
s1.issuperset(s2)
False
s1.issubset(s3)
False
s3.issubset(s1)
True
s1.isdisjoint(s2)
False
s4 = {7,8,9}
s1.isdisjoint(s4)
True
s1.difference(s2)
{1, 2, 3, 5}
>>> s1.symmetric_difference(s2)
{1, 2, 3, 5, 8, 9}
>>> s1.add(100)
>>> s1
{1, 2, 3, 4, 5, 6, 100}
>>> s1.pop()
1
>>> s1.remove(4)
>>> s1
{2, 3, 5, 6, 100}
>>> s1.remove(90)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s1.remove(90)
KeyError: 90
>>> s1.discard(5)
>>> s1.discard(90)
>>> s1.clear()
>>> s1
set()
