# basics-of-python

1. Python exectution order
A. create the function test
B. Create variable x
Call test()
3.Continue to next line

* "def"  only stores instructions. The code inside runs only when the function is called

--

2. print() vs return
print()

Shows a value on the screen.

return

Sends a value back to the caller.

--

3. Scope

Scope answers:

Which variable am I using?

x = 5

def test():
    x = 10
    print(x)

test()
print(x)

Output:

10
5

Local x and global x are different variables.

--

4. global
x = 5

def test():
    global x
    x = 10

test()
print(x)

Output:

10

global tells Python:

Use the global variable instead of creating a local one.

--

5. Scope vs Mutability

This was the biggest concept.

Scope

Answers:

Which object am I talking about?

Mutability

Answers:

Can this object be modified?

Python decides:

1. Scope first
2. Mutability second

--

6. Assignment vs Copy
Assignment
a = [1,2]
b = a

Both names point to the same object.

b.append(3)

print(a)  # [1,2,3]
Shallow Copy
a = [1,2]
b = a.copy()

Two separate outer lists.

b.append(3)

print(a)  # [1,2]
print(b)  # [1,2,3]

--

7. Parameters vs Arguments
def greet(name):
    print(name)

greet("Yash")
name → Parameter
"Yash" → Argument


--


8. Mutable Default Argument Trap
def add(item, lst=[]):
    lst.append(item)
    return lst

Calls:

add(1)
add(2)
add(3)

Output:

[1]
[1,2]
[1,2,3]

Because the default list is created only once when the function is defined.

Safe version:

def add(item, lst=None):
    if lst is None:
        lst = []

    lst.append(item)
    return lst

--

9. Introduction to OOP
class Dog:
    pass
Dog → Class (blueprint)
dog1 = Dog() → Object (instance)
