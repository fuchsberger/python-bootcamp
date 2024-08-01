# For Loops
For loops iterate over a sequence of objects and allow us to run a block of code for each object in the sequence.

For example, a loop can be used to go through a list of names and evaluate whether each name is uppercase or not.

Like if statements, a block of code associated with a for loop is defined using indentation. A for loop has the generalized syntax:

```python
for item in sequence:
    '''
    indented block of code
    that will run for each
    item in sequence
    '''
  ```
Refer to the "For loop" section in ["Control Flow" chapter of A Byte of Python](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fpython.swaroopch.com%2Fcontrol_flow.html)

```python
# Iterate over a range using the "range()" function
# The range function returns a sequence of numbers
for i in range(6):
    print(i)

# Iterate over a string
for letter in "Groundhog":
    print(letter)
```

> **Try it Yourself**: Write a for loop that uses the range function and an if statement to print out even numbers between 1 and 10.

```python
# For loops let you iterate over a list
departments = ["Biology", "Art History", "Accounting", "English", "Engineering"]

# Loop over the members of artist_names to print out the element and its length
for name in departments:
    print(name, len(name))
```

> **Try it Yourself**: Write a for loop that prints out the names that begin with the letter "K" in the list artist_names.

_Tip: If you're stuck, start by writing a for loop that prints out all of the artist names._

```python
# A list of artist names
artist_names = ["Picasso", "Klee", "Lawrence", "Kahlo", "O'Keeffe"]

# Write your for loop here:
```
