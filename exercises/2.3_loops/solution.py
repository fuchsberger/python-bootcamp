# Part 1
#Use a range() from 0 to 50
for i in range(50):
  # The modulo % shows you the remainder. if it's zero, then the number is evenly divisible by four.
  if i%4 == 0:
    print(i)


# Part 2
fruit_bowl = ["Apple", "Pear", "Banana", "Grapes", "Kiwi", "Mango", "Blueberries", "Peach"]

for fruit in fruit_bowl:
  if fruit[0] == "P" or len(fruit) <=4:
    fruit = fruit.upper()
    print(fruit)
