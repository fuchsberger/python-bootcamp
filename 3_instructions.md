# Day 3 Topics

## While Loops
For as long as a condition is true the loop will repeat executing the code block
```python
x = 0
while x < 10:
    x += 1
```
Like with for loops we can use `break` to exit a loop prematurily and `continue` to immediately jump to the next iteration.

## List Comprehension
[List comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) is a convenient way in Python to create a new list based on a filtered old list.

Instead of doing this:
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
```

one could simply create the new list in a single line:
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
```

> **Try it Yourself**:  Use list comprehension to create a list of all alphabetic letters that appear in the string.
>
>*Tip:* You will need a library function for this from [here](https://www.w3schools.com/python/python_ref_string.asp).
```python
# start with this string
s = "Python > Java!"

# Use List Comprehension and a library function to
# split the string into characters and
# filter out all non alphabethic characters.
# do it all in a single line
l = [???]

# Print the new string
# should print: ['P', 'y', 't', 'h', 'o', 'n', 'J', 'a', 'v', 'a']
print(l)
```

## Functions
You may have seen this by now, functions in Python are defined with the def keyword, followed by the name of the function and, in parenthesis a list of parameters:
```python
def welcome():
  print("Hi")

def welcome(name):
  print(f"Welcome, {name}!")
```

To call (execute / invoke) a function we need to provide the name, and fill arguments (values) into the expected parameters:
```python
welcome("Sam")
# Welcome, Sam!
```

### Return Values
Functions typically return a value, which can then be used and assigned in the scope they were called

```python
def fullName(first, last):
  return first + " " + last

fullName = fullName("Sam", "Adams")
```

It is also possible for a function to return multiple values:
```python
def flip(a, b):
  return b, a

b, a = flip(a, b)
```

It is also possible to have more than one return statement in a function.
The moment the computer executes a line with the return statement it immediatly exits the function and returns to the place it was called. Thus all code below  will never execute:
```python
def doThis(n):
  if n < 3:
    return n
  return n += 3

doThis(0) # 0
doThis(3) # 6
```


> **Try it!** Write a function `sum(list)` that takes a list of numbers and returns the sum of all the numbers in the list.
>
> **Optional Objective:** If anything other than a list was provided or if any element in the list is not a number return False
>
> **Example:**
> ```python
> sum([1, 2, 3])
> 6
> sum([1, 2, "hi"])
> False
> sum("Hi")
> False
> ```

### Optional Arguments
Python has a nifty feature where functions can have default values for inputs if you don’t give it the inputs.

```python
def myFunction(x, y, z):
        print("You gave me", x, y, z)
```
The above function insists that you call it with three arguments as seen here:

```python
myFunction(3, "hi", 2.34)
```

If you write a function where most of the time, the arguments will have a known value, you can assign that value in the function definition and not make the user type all the arguments.

``` python
def myFunction(x, y="hi", z=2.34):
        print("You gave me", x, y, z)
```
You can call the above function in the following ways:

```python
myFunction(2)                     # assumes y is “hi” and z is 2.34
myFunction(2,True)                # assumes z is 2.34
myFunction(2, True, "hello")      # just uses what you gave it
```

> **Try it!** Write a function named `optFunction` that takes `5` integers and adds them and prints the results. Make all 5 of them optional and let them have the value 0 when the function call doesn’t say. You should get the following results:
>
> |Function call|prints|
> |---|---|
> `optFunction()`|0
> `optFunction(6)`|6
> `optFunction(6,3)`|9
> `optFunction(6,3,1)`|10
> `optFunction(6,3,1,4)`|14
> `optFunction(6,3,1,4,2)`|16

## Nested Loops
A nested loop is a loop structure inside another:

```python
for i in range(3):
  for j in range(3):
    print(i * j)
```

In nested loops the inner loop gets executed in full for each iteration of the outer loop.


> **Reflect!** How many print statements get executed in total with the nested loop above? What is going to get printed?

Nested loops are in particular useful for 2D applications (tabular data, games, images) or data in general.

# Turtle Graphics

Lets start by checking out the content in tutle.py and running it...

You can run a specific python file via a command in the shell:
```bash
python myTurtle.py
```

For convenience we can import the correct turtle file in our main file which allows us to draw by clicking the Run button:
At the top of `main.py`:
```python
import myturtle
```

> **TODO** create your own python file named `turtle_loops.py` and import it in your main file. Uncomment the previous import.

### Exercise 1: Drawing Grid of circles
Our objective is now to combine what we know of nested loops with our drawing capabilities of turtle to draw a grid of circles. a 5x5 grid of circles should be sufficient.


### Exercise 2: Plus
Modify your nested loop so circles in the central horizontal and vertical lines are drawn in a dark color to simulate a plus.

### Exercise 3: X
Modify your nested loop so circles in on the diagonals are drawn in a dark color resulting in a X.
