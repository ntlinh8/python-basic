# In normal, the child class will inherit properties and methods of base class
# But, if you want to change this fact. Or you want the child class will inherit some properties and some methods instead of all properties and methods
# -> The solution is using the access modifier
# The access modifier will decied Can the property/method was inherited?
#
# Knowledge
# name: public property
# _name: protected property
# __private property
# This fact will be applied for both class and instance methods/properties

# The first, I have a Person class. All people in the world also have name and id cart
# But the name can was knew by everyone
# But the id cannot. If the other people know your id. Be careful
# So the id is a private property and name is a public property
# Both name and id are instance's properties

# In defaul, all class in python is inheriting the Object class
class Person:
    def __init__(self, name, __id, _gmail) -> None:
        self.name = name 
        self._gmail = _gmail
        self.__id = __id

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id



p1 = Person("Sunny", "GH123", "sunny@gmail.com")
print(p1.name) # You can directly get/set the name of this instance because name is a public property

#print(p1.__id) # You cannot directly get/set the id of this instance because id is a private property
# So, with the private property, we cannot to directly set/get it. We need to create a getter/setter method
# The private method only access in the class
# cannot access to the private property on outside class
print(p1.get_id())
p1.set_id("GHAD34")
print(p1.get_id())

# for the protected property, we can access to them by child class of them
# Example, directly access from the instance of class
print(p1._gmail)

# access to the protected propety by the instance of child class
class Employee(Person):
    def __init__(self, name, __id, _gmail) -> None:
        super().__init__(name, __id, _gmail)


e1 = Employee("Hanna", "SA234", "hannajackson@gmail.com")
print(e1._gmail)



