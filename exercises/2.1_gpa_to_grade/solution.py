# Add float() to convert the input to a numerical value instead of a string
num_grade = float(input("Enter your grade (0 - 100): "))

# Check if the user input is within 0 - 100
if num_grade > 100 or num_grade < 0:
  letter_grade = "INVALID"
# If the input is valid, check which grade range it is in
else:
  if num_grade >= 90 and num_grade <= 100:
    letter_grade = "A"
  elif num_grade >= 80 and num_grade < 90:
    letter_grade = "B"
  elif num_grade >= 70 and num_grade < 80:
    letter_grade = "C"
  elif num_grade >= 60 and num_grade < 70:
    letter_grade = "D"
  elif num_grade >= 0 and num_grade < 60:
    letter_grade = "F"

# Print the final result
print(letter_grade)
