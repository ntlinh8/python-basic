# In python, each variable is an object. Example
# when I define and agsign a value for a variable
# x = 1
# x is an instance or an object of integer class

# Define a class with properties and methods
# We have a person class.
# the constuctor of class is __init__ method
# If you don't define it, when create a instance of class, the default method were called

################################## The first class ###################################
class Person:
    def __init__(self, id, name):
        self.id = int(id)
        self.name = name

    def __str__(self):
        return f"{self.name}, {self.id}"

# We have a instance/object of Person class
p1 = Person(4, "Linh")

# After override the default method of class, when we access to this method the new method was called
print(p1)
print("This is ", p1.name, ". My id is ", p1.id)

################################ Class's Properties and Instance's Properties ##########################################
class Car:

    # This is not a variable of instances or object
    # This is class variable, we can call in from another class or module (depends about the access modifier (in next session))
    typeCar = "Small Car"

    def __init__(self, name, id, color, seatNumber, produceYear) -> None:
        self.name = name
        self.id = id
        self.color = color
        self.seatNumber = seatNumber
        self.produceYear = produceYear
    
    def get_car_name(self):
        return self._name

    def set_car_name(self, name):
        self._name = name

# Because typeCar is a class's property, so we can call this variable from class instead of instances
print(Car.typeCar)
Car.typeCar = "Big Car"
# print(Car.id)
# Because we never set the access modifier for this typeCar, so I can call this property from internal class, 
# or external class (also in the module), or the other class from another module
# For the 63th line, we cannot call to the id property because that is a instance's properties
# if you wanna call to the instance's properties, you need to define a instance of class, like this:
car = Car("Sujuki G12", "123GH21", "Black", 4, 2018)
# After define a instance of class, you can call to properies of instance and class
# the propeties of class also was called by instances. Because they was applied for all instances of class
# Call the instance's properties
print(car.id)
print(car.name)
print(car.color)
print(car.produceYear)
print(car.seatNumber)

# Access to the class's properties from instances
print(car.typeCar)

# Because these properties never setted the access modifier, so we can access to them from every where in the module

################################ Inheritance ##################################

# Firstly, I have a parent class. This is Animal class
# This class will contain some properties like: animalName, legNumber, eyeNumber, isFly
# and some methods like: eatting(), noicing(), 

class Animal:
    def __init__(self, animalName, legNumber, eyeNumber) -> None:
        self.animalName = animalName
        self.legNumber = legNumber
        self.eyeNumber = eyeNumber

    def eatting(self, typeOfFood):
        print("This is ", self.animalName, " and I'm eatting ", typeOfFood)

    def noicing(self, noice):
        print("This is ", self.animalName, " and I'm ", noice)

# So I have some type of animals, and they will inheritance the Animal class
class Bird(Animal):
    def __init__(self, animalName, legNumber, eyeNumber, flyHeigh) -> None:
        super().__init__(animalName, legNumber, eyeNumber)
        self.flyHeigh = flyHeigh
    
    def flying(self):
        print("A bird is flying")

class Dog(Animal):
    def __init__(self, animalName, legNumber, eyeNumber, isFriendly) -> None:
        super().__init__(animalName, legNumber, eyeNumber)
        self.isFriendly = isFriendly

# So, I will create the instance of dog class and bird class
dog = Dog("Bob", 4, 2, True)
bird = Bird("Jennan", 2, 2, 1500)

# I can access to the method of animal class because this method was inheritanced by child class
dog.eatting("meat")
bird.eatting("nut")
dog.noicing("go go")
bird.noicing("chip chip")

# and for the unique method for class (like flying())
bird.flying()


    






