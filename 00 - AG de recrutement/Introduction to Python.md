<img src="https://insalgo.fr/assets/images/logos/logo.svg" style="height:64px;margin-right:32px"/>

### Introduction to Python

Python is a high-level, readable, dynamically-typed programming language used for web development, data science, automation, and more. Python code usually ends in `.py`.

***

### Hello World

```python
print("Hello, world!")
```

This outputs:
`Hello, world!`

***

### Variables \& Data Types

- Numbers (integers, floats)
- Strings
- Booleans

```python
x = 10         # integer
y = 3.14       # float
name = "Ada"   # string
is_active = True  # boolean
```


***

### Comments

Single-line comments in Python use `#`.

```python
# This is a comment
```


***

### Basic Math

```python
a = 5 + 3   # 8
b = 2 * 6   # 12
c = 5 / 2   # 2.5
d = 5 // 2  # 2 (integer division)
e = 2 ** 3  # 8 (exponent)
```


***

### Strings

```python
greeting = "Hello"
who = "World"
message = greeting + ", " + who + "!"
print(message)  # Hello, World!
```

- String formatting:

```python
age = 23
print(f"I am {age} years old")  # I am 23 years old
```


***

### Lists

```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])    # apple
fruits.append("pear")
print(fruits)       # ['apple', 'banana', 'orange', 'pear']
```


***

### Dictionaries

```python
person = {"name": "Alice", "age": 30}
print(person["name"])        # Alice
person["age"] = 31
```


***

### If Statements

```python
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")
```


***

### Loops

```python
# For loop
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 3:
    print(count)
    count += 1
```


***

### Functions

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ada")   # Hello, Ada!
```


***

### Importing Modules

```python
import math
print(math.sqrt(16))  # 4.0
```


***

### Basic File I/O

```python
# Writing
with open("sample.txt", "w") as f:
    f.write("Hello, file!")

# Reading
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
```


***

### Error Handling

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```


***

### Quick Summary Table

| Concept | Example |
| :-- | :-- |
| Print | `print("Hello")` |
| Variable | `x = 5` |
| List | `fruits = ["apple", "pear"]` |
| Dict | `d = {"key": "value"}` |
| If-else | `if x == 1: ... else: ...` |
| For loop | `for i in [1,2,3]: ...` |
| Function | `def foo(): ...` |
| Import | `import math` |


***

This covers the core Python syntax and features needed to get started programming in Python. Practice by writing small scripts and experimenting to reinforce your learning!

***

### Next Steps

- Learn about Python packages (pip install)
- Explore classes and object-oriented programming
- Read official docs at [python.org]

***

### A few project ideas!

- Number Guessing Game
- Rock, Paper, Scissor
- Simple To-Do List
- Calculator