# Python Syntax
Python is a widely used, flexible, open source, object-oriented programming language. We will be using Python 3, which is the most recent version of Python and isn't compatible with older versions of Python.

There are two concepts that we will use to show other topics in our lessons.

1. Comments are a way to write information and context for your code. Comments are lines of code that are not executed.
2. `print()` statements are a way to display information as output. It will help us test and develop our code.

```python
# This line is a comment, so nothing happens
# The next lines are print statements that create output
print("Hello world")
print(4+6)
```

# Variables
Variables store values for us to use at different points in our code, allowing us to access and change values as we need them.

Variable names:

- can contain letters (A-Z, a-z), numbers (0-1), and underscores (_)
- **cannot** contain spaces or begin with a number

```python
# Examples of variables:
x = 3
x = 3 + 7
title = "Ghostbusters"

# Python uses specific indentation
if 3 > 5:
  print("Hello world")
```

# Data Types
Today we will be covering "Primitive" data structures: integers, floats, booleans, and strings

- All primitive data structures are `immutable` and cannot be changed. When we change the value of a variable, we are really assigning a new value.
- Internally all primitives are implemented as classes.

  This allows things such as comparisons (<, <=, >, >=), arithmetic operations (+, -, *, /) and print().
- Additional resource: DataCamp [_Python Data Structures Tutorial_](https://www.datacamp.com/community/tutorials/data-structures-python)


## Integers

- Store whole numbers with no decimal points

```python
# Integer
x = 5 # assignment
x = 6 # reassignment

# You can check the type using type()
type(x) # Will return <class 'int'>
```
## Floats
- Store decimal numbers
- Are approximate and thus not entirely accurate. Arithmetic operations can lead to rounding errors.
- Consume the same amount of storage as integers

```python
x = 5.0
y = 4.4342233432

# You can check if a variable is of a type with isinstance()
isinstance(x, float) # will return True because x is a float

y = int(3.5) # int() can be used for assignment or conversion
y = str(3.5)
```

- You can use mathematical operations on integers and floats:
  - addition `+`
  - subtraction `-`
  - multiplication `*`
  - division `/`
  - exponents `**`
  - floor division (rounds down to the nearest integer) `//`
  - modulus (remainder only) `%`

When mixing integers and floats in a division python always creates floats:
```python
x = 10
y = 2.0
z = x / y        # z will be 5.0
```

> **Try it Yourself**: Use the mathematical operations above to calculate 400 times 4, divided by 14, plus 39? And what data type will the output be? Test your guess using a Python function.

## Booleans

Booleans are either `True` or `False` (note capitalization)
```python
x = True

# often used in conditional checks:
if(x == True):
  # do this

# when checking if something is true you can skip the == True:
if(x):
  # do this
```

## Strings

- Strings are groups of characters, similar to words.
- They are surrounded by quotes (either single quotes 'a string' or double quotes "a string"). It is the programmer's choice whether to use `"` double or `'` single quotation marks in strings, just be consistent.
- Remember that strings are immutable, which means that they cannot be changed after you have created one.
- Strings have a numerical index that starts at zero

```python
# String
greeting = "Hello everyone"

# Find a character in a string by index
# index 4 will return the fifth character: H[0] e[1] l[2] l[3] o[4]
greeting[4]

# You can slice a string to index multiple characters
greeting[1:3]

# Strings are immutable so you can't for example replace a character inside the string:
greeting[0] = "h"
```

> **Try it Yourself**:  Print the second character of this string:
```python
myString = "It is January"

#Print the second character of the string
```

### String Methods

Strings provide lots of methods (functions defined to work on class instances). Find a complete list of string methods on the [W3Schools String Methods](https://www.w3schools.com/python/python_strings_methods.asp) page

```python
greeting.capitalize() # Converts the first character to upper case
greeting.replace("Hello", "Goodbye") # Returns the string with the first parameter replaced with the second one

# Notice that neither of those methods changed the original string
print(greeting)

len(greeting) # Returns the number of characters in a string, or other data type

# We have methods that work on individual characters as well:
ord('h') # Will return the unicode index of the character (104)
chr(104) # Will return the character given a unicode index ("h")
```

### Formatting
You can combine multiple strings using concatenation:

```python
word1 = "chocolate"
word2 = "cake"

print(word1 + " " + word2 + "!")
```

Strings can also be formatted by prepending `f` and using `{}` to insert placeholders:
```python
cost1 = 546.343434
cost2 = 23546
print(f"The cost was $ {cost1:0.2f}!")
print(f"The cost was $ {cost2:0.2f}!")

# Output
# The cost was $   546.34!
# The cost was $ 23546.00!
```
> **Try it Yourself**:  Use indexing and concatenation to:
> 1) get the sixth character contained in the string `my_string`.
> 2) create a new variable with the following text: `The sixth character in this string is [character goes here]`.
> 3) Print the result.
>
>*Tip:* Characters include spaces.
```python
# Start with this string
my_string = "The sixth character in this string is"

# Create a new variable, set equal to the string above concatenated with a
# space and the sixth character in the string


# Print the new string
```



### Escaping Characters

Some characters that you may want to use in a string as also meaningful to Python (for example, quotation marks). If you want to include those characters in your string, you have to include `\` before the character.

```python
text = "We said: \"Life is good.\""
```
In a similar style you can use other escape characters:
- `\n` new line (affects console output)
- `\t` tab (less important nowadays)
