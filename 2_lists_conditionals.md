# Lists
A list holds a sequence of items. Lists can contain many different data types as list items. To reference a list item, you use the index (starting at zero, the same as a string).

To learn more about lists:
- ["Data Structures" chapter of A Byte of Python](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fpython.swaroopch.com%2Fdata_structures.html)
- [Python documentation for lists](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.python.org%2F3%2Ftutorial%2Fintroduction.html%23lists)

```python
# An example of a list of strings
assignments = ["Homework", "Quiz", "Research Paper"]

# Lists can contain multiple data types
example = ["Homework", 3, 5.6, ["list", "of", "lists"]]

# Get a list item by index
print(assignments[2])

# Replace an element "in place" via its index
assignments[2] = "Final"
```

## List Methods
Unlike strings, lists are mutable and can be changed after creation. Some list methods alter the existing list while some return a new value.

[Full list of Python list methods](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fwww.w3schools.com%2Fpython%2Fpython_ref_list.asp)

```python
# Add "Final project" to the end of the "assignments" list (append list method)
assignments.append("Final project")

# Count the number of elements with the value "Final project" in the list
assignments.count("Final project")

# Remove first occurrence of value in the list (remove list method)
assignments.remove('Quiz')
```
> **Try it Yourself**: Try it Yourself: Replace the list item "orange" with "pear."
> ```python
>fruit = ["banana", "orange", "apple"]
> ```
>**Bonus Try it Yourself:** Print the value "g" from the list letter_list.
> ```python
> letter_list = ["a", "b", "c", ["d", "e"], ["f", "g"]]
> ```

# Conditionals

Conditionals allow you to execute a block of python code only if a certain condition is met. You can add additional conditions and code if you want to.

To create those conditions, you will need to use comparison and logical operators.

## Comparison Operators
Comparison operators are used to compare two values and return a value of True or False, a boolean data type. They are often used in if statements.

The following are Python comparison operators: ==, !=, >, <, >=, <=

Note: To compare two values, make sure to use ==. A single = is used for assignment, like creating variables.

```python
# Compare numbers
print(5 > 2)
print(5 == 2)
print(5 != 2)
print(5 >= 5)

# Compare strings
print("This string" == "This string")
print("This string" == "this string")

# Compare other expressions using multiple data types
len("Octopus") == 2-5
```

> **Try it Yourself**: What is the result of this comparison?
>_Hint: Remember that lists are surrounded by square brackets._
>```python
>len([1, 2]) == 2
> ```

## Logical Operators
Logical operators are used to evaluate multiple conditional statements and return a value of True or False, a boolean data type. They allow us to combine the results of multiple comparisons.

The following are Python comparison operators: and, or, not

- and checks if both conditions are true
  - <img src="https://raw.githubusercontent.com/ncsu-libraries-data-vis/introduction-to-programming-with-python/main/images/venn_diagram_and.png" alt="A venn diagram labeled 'and' with the middle, overlapping section shaded in. Shows that 'and' is true only when both conditions are met." width="75%"/>
- or for at least one condition to be true
  - <img src="https://raw.githubusercontent.com/ncsu-libraries-data-vis/introduction-to-programming-with-python/main/images/venn_diagram_or.png" alt="A venn diagram labeled 'or,' with both circles completely filled in. Shows that 'or' is true if either of the two conditions are met or both conditions are met." width="75%"/>
- not checks for the opposite of the condition

```python
num = 5
# The "and" operator checks if both conditions are True
num > 3 and num < 10

# The "or" operator checks if at least one of the conditions are True
num > 3 or num < -3
```

>**Try it Yourself:** Write a statement that checks if a number is less than 10 and greater than zero.

There is also the **not** operator. It allows you to negate a condition for example:
```python
5 not in [1, 2, 3]
# will be True
```

To learn more about logical and comparison operators:
["Operators and Expressions"](https://python.swaroopch.com/op_exp.html) chapter in a Byte of Python


# If statements

"The if statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block). The else clause is optional." (From the "If Statements" section of the "Control Flow" chapter of A Byte of Python)

A block of code associated with an if statement is defined using indentation. A basic if statement has the following generalized syntax:

```python
if conditional_expression:
    '''
    indented block of code
    that will run when
    conditional_expression equals true
    '''
```
We can chain several conditional blocks together as well:
```python
if(condition):
  # do this
else:
  # otherwise do that


if(condition1):
  # do this if condition1 is met
elif(condition2):
  # or do this if condition2 is met
else:
  # otherwise do that


if(condition1):
  # do this if condition1 is met
elif(condition2):
  # or do this if condition2 is met

```
> **Try It Yourself:** There are 24 seats in a classroom. Write an if statement that prints out a message based on how many class members there are.
>- If there are 24 students, print "The class is full."
>- If there is at least one student, but fewer than 24 students, print "Would you like to join the class?"
>- If there are more than 24 students print, "Oh no, there aren't enough seats for everyone!"
