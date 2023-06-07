# The Polymorphism is the provision of a single interface for all class which was inheritanced it
# Like the example in previous session
# So, I'll create the base class with the base method (but cannot implement)
# When the child class inheritances this class, they will implement this methods
# Depend on the child class, the action in this method will be created
# So, in the child class, we don't need define a new method, we only access to this method and implement it
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
