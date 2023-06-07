# In python, each variable is an object. Example
# when I define and agsign a value for a variable
# x = 1
# x is an instance or an object of integer class

# Define a class with properties and methods
# We have a person class.
# the constuctor of class is __init__ method
# If you don't define it, when create a instance of class, the default method were called

class Person:
    def __init__(self, id, name):
        self.id = int(id)
        self.name = name

    def __str__(self):
        return f"{self.name}, {self.id}"

class Student(Person):
    def __init__(self, id, name, className):
        super().__init__(id, name)
        self.className = className
    def learning(self):
        print("I'm learning in ", self.className)


p1 = Person(4, "Linh")
print("This is ", p1.name, ". My id is ", p1.id)
print(p1)

s1 = Student(int(18), "Linh Nguyen Thuy", "Automation Group")
print("My student id is ", s1.id)
print("My student name is ", s1.name)
print("My student class is ", s1.className)

