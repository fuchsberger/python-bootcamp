# Start with these variables
classes = "This fall I'm taking Intro to Art History, Data Structures, and Data Ethics."
year = 2024
university = "Bucknell"

# Part 1
# Use the .replace() method to replace a single word
# String are immutable, so save it in a new variable to keep the changes
springClasses = classes.replace("fall", "spring")
print(springClasses)

# Part 2
# Use the ord() function to find the unicode value
uni = ord("e")
# Use an f string or contatenation to combine the result with a string
# You can't combine strings and integers, use the str() function to convert another data type to a string
print("The unicode index for 'e' is " + str(uni) + ".")

# Part 3
# Use a formatted string and include the variables in curly brackets
print(f"In {year} I will be attending {university}. {springClasses}")
