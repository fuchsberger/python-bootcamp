# GPA to Grade

Write a program that takes a student's grade on a scale from 0 to 100, and prints their letter grade. To keep your code from getting longer than it needs to be, we won't use pluses or minuses. Use the following mapping:

- **A:** greater than or equal to 90 and less than or equal to 100
- **B:** greater than or equal to 80 and less than 90
- **C:** greater than or equal to 70 and less than 80
- **D**: greater than or equal to 60 and less than 70
- **F:** greater than or equal to 0 and less than 60

If the user inputs any number greater than 100 or less than 0, it should output `INVALID`

**Input:**

- num_grade: a number from 0 to 100

**Output:**

- the corresponding letter grade (`A`, `B`, `C`, `D`, or `F`) for a valid number, `INVALID` for an invalid number

## How it Should Work..

```
Enter your grade (0 - 100):  90
A
```

```
Enter your grade (0 - 100):  89.999
B
```

```
Enter your grade (0 - 100):  70
C
```

```
Enter your grade (0 - 100):  34
F
```

```
Enter your grade (0 - 100):  101
INVALID
```
