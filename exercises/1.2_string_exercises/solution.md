myString = "You need parentheses for chemistry !"

# Part 1
# Use slicing and indexing
print(myString[31:34])
# or use negative indexing to count from the end of the string
print(myString[-5:-2])

# Part 2
# Use slicing and indexing
print(myString[0:8])
# Or leave out the start value to indicate starting at the very beginning of the string
print(myString[:8])

# Part 3
# Use the stride value to skip an index
# You can include a start and end point, or you can leave them blank if it's the very beginning and very end of the string
print(myString[::5])

# Part 4
# You can use a negative stride to print backwards
print(myString[::-1])

# Part 4
# Gather user input using the input() function
userString = input("Type a string:")
# Calculate the halfway point by finding the length and dividing by 2
# Indexes must be whole numbers, so use floor division
half = len(userString)//2
# Find the first half by using the variable 'half' as the end point
firstHalf = userString[:half]
#print the results
print(firstHalf)
