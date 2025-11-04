---
marp: true
---
<!-- class: invert -->

# Python Codegolf Cheatsheet

---
## Conditions
### Inline conditions
```python
if X:
    print(A)
else:
    print(B)
```
40 characters

```python
print(A if X else B)
```
20 characters

---
### AND conditions
```python
if X and Y:
    print(A)
else:
    print(B)
```
46 characters

```python
print([A,B][X and Y])
```
21 characters

And even better with **bitwise operators
```python
print([A,B][X&Y])
```
17 characters!

---
### Smart split
You can leave the space out before an operator if it is preceded by a number
```python
print(5<X and Y<5)
```
18 characters

```python
print(X<5and Y<5)
```
17 characters

---
### Multiple comparisons
```python
print(0<X and X<5)
```
18 characters

```python
print(0<X<5)
```
12 characters

And even better:
```python
print(X<5and Y<5)
```
17 characters

```python
print(X<5>Y)
```
12 characters

---
But why stop here??
```python
print(X>0and Z>0and Y<X)
```
24 characters

```python
print(Z>0<X>Y)
```
14 characters!!

---
### Multiple equalities
You can use tuples to compare multiples values
```python
print(X==5and Y==6 and Z==7)
```
30 characters

```python
print((X,Y,Z)==(5,6,7))
```
23 characters


⚠️This does not save space for only two comparisons

---
### Booleans
In Python, booleans are also integers
```python
print([5,9][X])
```
15 characters

```python
print(5+4*X)
```
12 characters

Difference of one
```python
print([5,6][X])
```
15 characters

---
```python
print(5+X)
```
10 characters

First num is one
```python
print([1,6][X])
```
15 characters

```python
print(6**X)
```
11 characters

---
Of course, this is Python so it also works with strings!
```python
print(['hello','world'][X])
```
27 characters

```python
print(X*'world'or'hello')
```
25 characters

---
### Evil string indexing
The full slicing operator syntax is as follow:
```python
array[start:stop:step]
```
The default values if ommitted are: 
```python
start = 0
stop = -1
step = 1
```
The step value can be very useful!

---
```python
print(['YES','NO'][X])
```
22 characters

```python
print('YNEOS'[X::2])
```
20 characters

And we can keep going:
```python
print(['hello','world','fish'][X])
```
34 characters

```python
print('hwfeoilrsllhod'[X::3])
```
29 characters

---
## Output

```python
print(', '.join(['A','B']))
```
27 characters

```python
print(*'AB',sep=', ')
```
21 characters

To list the alphabet letters
```python
import string
print(string.ascii_lowercase)
```
44 characters

---
```python
string=[chr(i+97)for i in range(26)]
```
36 characters

```python
string='abcdefghijklmnopqrstuvwxyz'
```
35 characters

```python
string=map(chr,range(97,123))
```
29 characters

---
## Loops

Simple inline loops:
```python
a=[]
for i in range(10):
    a.append(i)
```
42 characters

```python
a=[i for i in range(10)]
```
24 characters

---
Always avoid nested loops!

```python
for a in range(3):
    for b in range(5):
        print(a,b)
```
62 characters

```python
for a in range(X*Y):print(A//X,a%X)
```
35 characters

---
You can even do it with three or more loops:
```python
for i in range(5):
    for j in range(6):
        for k in range(7):
            print(i,j,k)
```
96 characters

```python
for k in range(5*6*7):
    print(k//6//7, k%(6*7), k%7)
```
56 characters

---
And if you loop less than 4 times:
```python
for a in range(4):func()
```
25 characters

```python
for a in 0,1,2,3:func()
```
23 characters
This is also useful when you need `step != 1`

---
If the value of `a` doesn't matter:
```python
for a in range(10):func()
```
25 characters

```python
for _ in [1]*10:func()
```
22 characters

And the reason why interpreted languages are the best:
```python
exec("foo();"*10)
```
17 characters

---
## Variables

### Functions
```python
def c(a):
    return a+1
```
25 characters

```python
c=lambda a:a+1
```
14 characters

---
### Iterables unpacking
Here you can replace `range(10)` with most iterables
```python
A=list(range(10))
```
17 characters

```python
*A,=range(10)
```
13 characters

---
Same thing with multiple variables:
```python
l='abcdef'
A=l[0]
B=l[2]
C=l[3:]
```
35 characters

```python
A,_,B,*C='abcdef'
```
17 characters

---
This is also useful for long function names:
```python
a,b,c=input(),input(),input()
```
29 characters

```python
i=input;a,b,c=i(),i(),i()
```
25 characters

---
Or with eval():
```python
a,b,c,d,e=input(),input(),input(),input(),input()
```
49 characters

```python
a,b,c,d,e,_=eval("input(),"*5+'0')
```
34 characters

---
## Iterables

### Lists
Most "normal" list operations can be shorter:
```python
# List creation
A,B=4,[] #8 chars
A,*B=4, #7 chars

# Getting first item
A=L[0] #6 Chars
A,*_=L #6 Chars

# Getting last item
A=L[-1] #7 Chars
*_,A=L #6 Chars

# Removing first item
L.pop(0) #8 Chars
L=L[1:] #7 Chars
_,*L=L #6 Chars

# Removing last item
L=L[:-1] #8 Chars
L.pop() #7 Chars
*L,_=L #6 Chars
```

---
```python
# Appending an item
L.append(A) #11 Chars 
L+=[A] #6 Chars
L+=A, #5 Chars

# Extending a list
A.extend(B) #11 Chars 
A+=B #4 Chars

# Inserting items into a list
L.insert(i,A) #13 Chars 
L[:i]+=A #8 Chars

# Reversing a list
L=L.reverse() #13 Chars 
L=L[::-1] #9 Chars
```

---
A very elegant way to iterate on a list in reverse using bitwise operators:
```python
L[::-1][A]
```
10 characters

```python
L[~A]
```
5 characters

---
### Conversion of iterable to list
You might need this to call len() for example
```python
print(len(list(A)))
```
19 characters

```python
print(len([*A]))
```
16 characters

---
### Sets
Python sets have operators very similar to the bitwise operators:

```python
setA|setB # Union
setA&setB # Intersection
setA-setB # Difference 
setA^setB # Symmetric difference (XOR)
```

There are also variants with = for in-place operations:
```python
setA|=setB # Union
setA&=setB # Intersection
setA-=setB # Difference
setA^=setB # Symmetric difference (XOR)
```

---
Here is how to check if an element is in a set:
```python
var in setA
```
11 characters

```python
{var}&setA
```
10 characters

---
## Operators

### Bitwise operators
`-~n`is equivalent to n+1
`~-n`is equivalent to n-1
This can be combined with other operators to gain more characters

### Boolean operators
Here are a few more operator alternatives
```python
a and b
a*b
a&b
```

```python
a or b
a|b
```

---
### Math operators
```python
x=math.floor(A/B)
```
17 characters

```python
X=A//B
```
6 characters

And same technique for ceil:
```python
X=math.ceil(A/B)
```
16 characters

```python
X=-(-A//B)
```
10 characters

---
And for square root
```python
X=math.sqrt(A)
```
14 characters

```python
X=A**.5
```
7 characters

---
There are many more techniques to use, just make sure to practice!

# Sources
https://www.codingame.com/blog/code-golf-python/

https://www.geeksforgeeks.org/python/code-golfing-in-python/