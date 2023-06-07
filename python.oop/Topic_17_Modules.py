# A module is a .py file
# In the module, there are some classes. And classes can depend the other class. No problem
# I have a module and in this module, there are 4 classes: vehicle, car, boat, plane. 
# The 3 classes of end are inherit the vehical class

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
