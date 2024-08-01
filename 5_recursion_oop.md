# Day 5 Instruction


## Recursion

Recursion is simple to define but (sometimes) hard to understand:
> _A recursive function is a function that calls itself. Example:_
```python
def doThis():
  doThis()
```

A recursive function can often used interchangable with iteration. These two programs will do the same:
```python
for x in range(1, 4):
  print(x)
```

```python
def doThis(x = 0):
  if x <= 3:
      print(x)
      doThis(x+1)

doThis()
```
Based on the example above it seems iteration is simpler. So why recursion?
> Recursion allows us to do things we can't do with iteration, such as branching out into differnet blocks simultaniously.
>
> Internally in the computer recursion works a lot differntly than iteration. Recursion is more memory intensive as it "remembers" past cycles and allows us to interact with them. Iteration is like "forgetting what we did" after each time we repeat looping.
>
> Infinite Loops (Iteration) can cause your program to freeze.
> Infinite Loops (Recursion) raise an exception after going 5000 levels deeps.

### Structure
Every recursive function needs, what is called a _"base case"_. It guarantees the function will eventually exit.

```python

def power(number, exponent):
    # base case 1
    if exponent == 0:
        return 1

    # base case 2
    if exponent == 2:
        return number

    # recursive case
    return number * power(number, exponent - 1)

print(power(2, 3))
```
> Try the function above!

A function can have more than one but needs at least one 1 base case. Sometimes it is not immeadiatly evident what the base case is because the recursive case is conditional instead.


### Recursion Activity: Palindrome

_You may NOT use any for loops or while loops. You MUST use recursion_

Write a function - `is_palindrome` - that determines whether a given string (word) is the same forwards and backwards.

- It should return `True` if it is a palindrome
- It should return `False` if it is NOT a palindrome.

Examples:

```bash
>is_palindrome("racecar")
True
```

```bash
>is_palindrome("tool")
False
```

```bash
>is_palindrome("abba")
True
```

### Your Turn: Factorial (recursive)
The factorial (an important concept in math) is defined as:
```
factorial(6) = 6 * 5 * 4 * 3 * 2
```

Write a function `factorial(n)` that takes a number and returns the correct factorial.

### Your Turn: Fibonacci (recursive)
The fibonacci sequence is a special series of integers that goes like this:
```python
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```
For indexes 0 and 1:
- fib(i) = i

For all other indexes:
- at a given index `i` the  fibonacci number is `fib(i-1) + fib(i-2)`

Can you complete the recusive function in `fibonacci.py` using the information above?

### Binary Search & Efficiency

For this section please open [this jamboard](https://jamboard.google.com/d/1Qmp2kUq3Mcx8mvZNBuGmx7rWWnOSN2GRH6VZzR14nBA/edit?usp=sharing) in a new tab, i need to show you some hand-written notes.

Lets inspect and discuss the code in `binary_search.py` in a little more detail.

If i have a list of numbers given i could simply determine if an element exists within a sorted list this way:
```python
elements = [1, 3, 8, 11, 12, 15]

# We want to find the index of 12, should it exist, in elements
def search(elements, number)
    for i in range(len(elements)):
        if elements[i] == number:
            return i

    return None

search(elements, 12)
```
This code doesn't looks simple and is easy to understand compared to what we find in `binary_search.py`. Still the much longer code in binary search is much more efficient than the simple function above and thus should be used. Why?

## Classes
Classes are templates for creating objects and describe how an object should be structured and behave:
```python
class Item:
  # constructor
  def __init__(self, name, quantity=1, price=None):
    self.name = name
    self.price = price
    self.quantity = quantity

  # functions inside classes are called methods
  def total_price(self):
    return self.price * self.quantity
```

You can create instances of Item using the `new` keyword:
```python
bananas = Item("Banana", 5, 0.4)
print(bananas.total_price())
# 2.0
```

You can check if an instance is of type `Item`:
```python
print(isinstance(bananas, Item)) # True
```

Printing objects by default returns the object id:
```python
print(isinstance(bananas, Item))
# <__main__.Item object at 0x7f3f31bbff70>
```

We can customize what prints using the `print()` function:
```python
class Item():
  # ...

  def __str__(self):
    # this must return a string, not print something!!
    return f"{self.quantity} {self.name} for {self.price} each."

print(isinstance(bananas, Item))
# 5 Banana for 0.4 each.
```
This is also called overloading as we replace the default `__str__` method. We can overload other methods:
- `__lt__` lesser than. this allows us to do this: `item1 < item2`
- `__eq__` equal to. this allows us to do this: `item1 == item2`
- more here: https://stackabuse.com/overloading-functions-and-operators-in-python/

### Inheritance
Classes can be based on another class:

```python
class Item:
  def __init__(self, name, quantity=1, price=None):
    self.name = name
    self.price = price
    self.quantity = quantity

class Fruit(Item):
  def __init__(self, name, quantity=1, price=None, regional=False):
    # do not redo everything again, instead just call the parent's class constructor
    super().__init__(self, name, quantity, price)
    self.regional = regional
```

This is very useful if two objects are similar but have some distictive features. Inheritance allows us to avoid rewriting a lot of code.

A Fruit object is both a `Fruit`, as well as an `Item`:
```python
print(isinstance(apple, Fruit)) # True
print(isinstance(apple, Item)) # True
```
A fruit has access to all methods of the parent class.

Redefining a method in the subclass allows us to overwrite the method of the parent class.
