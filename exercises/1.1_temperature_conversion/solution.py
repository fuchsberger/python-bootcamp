# Input the temperature in Celsius
# Store that answer in a variable
temp_c = float(input("Enter the temperature in C: "))

# Convert the temperature from Celsius to Fahrenheit by
# multiplying by 9, dividing by 5, adding 32
temp_f = temp_c*9/5+32

# Print the result in Farenheit
print(str(temp_f) + " F")

# Bonus Exercise: add a function
def celsius_to_fahrenheit(celsius):
  # Ask the user for a temperature in Celsius
  temp_c = float(input("Enter the temperature in C: "))

  # Convert the temperature from Celsius to Fahrenheit by
  # multiplying by 9, dividing by 5, adding 32
  temp_f = temp_c*9/5+32

  #return the result in Farenheit
  return(temp_f)
