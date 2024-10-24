# Temperature Conversion


In Python we can get some user input using the `input` function:
```python
text = input("Type something: ")
print(text) # this will print whatever you typed.
```

Now inspect the starting code given in `main.py`.
```python
temp_c = float(input("Enter the temperature in C: "))
```
Can you figure out what is happening here?

### Assignment

Use the starting code to write a program in which someone enters the current temperature in Celsius and the program returns the number in Fahrenheit.

To convert temperatures in degrees **Celsius to Fahrenheit**, multiply by `9`, divide by `5`, and then add `32`.

**Input:**
- The current temperature in Celsius (an  integer or float)

**What you'll print (output):**
- The current temperature in Fahrenheit rounded to 1 decimal.

### How it should work
```
Enter the temperature in C: 0
32.0 F
```

```
Enter the temperature in C: 100
212.0 F
```

```
Enter the temperature in C: 50
122.0 F
```

### Bonus Exercise
If you feel confident, you can put the temperature conversion into its own function and call it:
```python
def celsius_to_fahrenheit(celsius):
  pass
```
