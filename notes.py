person = {
  "Name": "Sam Adams",
  "Age": 20
}

class Person:
  def __init__(self, name, age = None):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Person ({self.name}, {self.age})"

class Student(Person):
  def __init__(self, name, age=None, gpa=None):
    # self.name = name
    # self.age = age

    super().__init__(name, age)
    self.gpa = gpa

  def __str__(self):
    return f"Student ({self.name}, {self.age}, GPA: {self.gpa})"

p1 = Person("Sam Adams", 20)
p2 = Student("George Washington", 72, 2)

print(isinstance(p1, Person))

print(isinstance(p2, Student))
print(isinstance(p2, Person))


























# class Stack:
#   def __init__(self, name=None):
#     self.name = name
#     self.items = []

#   def __str__(self):
#     return f"Stack (type: {self.name}, {len(self.items)} items, top: {self.peek()})"

#   def peek(self):
#     if len(self.items) == 0:
#       return None
#     else:
#       return self.items[-1]

#   def push(self, item):
#     self.items.append(item)

#   def pop(self):
#     return self.items.pop()

# food_items = Stack("Food")
# sport_items = Stack()

# # test stack
# food_items.push("A")
# food_items.push(1)
# food_items.push(False)

# print(food_items)
# print(sport_items)


# # #  Stack (First In Last Out)
# # # Adding items: 1 > 2 > 3
# # #
# # #                        3
# # #             2          2
# # #    1        1          1
# # #   ____     _____     _____

# # # push, pop
# # #
