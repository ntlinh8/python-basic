# Dictionaries are used to store data values in key:value pairs

# Create a dictionary
from re import U


user_1 = {
    'name': 'Elon Musk',
    'company': 'SpaceX',
    'id': 123321123,
    'year of birth': 1992,
    'year of birth': 1993,
    'favorite fruits': ['banana', 'apple', 'cherry']
}

# Access Items
# There are many way to get the item/key/value from the dictionary

# 1. get value by key
# 1.1. using the key like a index of the dictionary
# If the dictionary contains the item that have a same key, the last value will access
print('Print the value of item by key: ', user_1['favorite fruits'])
print('Print the value of item by key: ', user_1['id'])
print('Print the value of item by key: ', user_1['year of birth'])
# 1.2. using get method, if the key not exist, return None for get method
print('Print the value of item by get method: ', user_1.get('id'))
print('Print the value of item by get method: ', user_1.get('gmail'))

# 2. get all key of dictionary -> return a list which contains all keys
print('Get all key of dictionary: ', user_1.keys())
# Warning: if you using get all keys by keys() method, 
# this method will return a list which will reference to the memory area contains all keys
# so, after define a key list, if you add items to the dictionay, the list also contains new keys of new items
# Please see the example following:

# I have a car dictionary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
# get all properties of car object
properties_car = car.keys()
# Print all key of car
print('Key of car is ', properties_car) 
# add new item to the dictionary
car["color"] = "white"
# Print all key of car
print(properties_car) 
# You can see the properties_car will contains 'color' properties

# 3. Get all values of the dictionary with values() method
# as the same keys() method, values() also return the list that contains all keys of dictionary
# actually, this list will reference to the memory area that contains value
# so, it have a property like keys() method

# 4. Get items with items() method
# this method will return each item in a dictionray as tuple in a list
# Like keys() and values() methods, the items() method also reference to the memory area of the all tiems 
print('Get items in dictionary: ', user_1.items())

# 5. Check key exist in the dictionary
print('is Exist key in dictionary: ', 'gmail' in user_1)
print('is Exist key in dictionary: ', 'id' in user_1)

# 6. Change Values
# 6.1. Override value of the item
# You can change the value of a specific item by referring to its key name
# if this key doesn't exist, the item with new key will be created
user_1['company'] = 'twister'
print('Print the user_1 dictionary: ', user_1)

# 6.2. In the way 2, you can use the update() method
user_1.update({'gmail': 'elonmusk@gmail.com'})
print('Print the user_1 dictionary: ', user_1)

# 7. Remove item from the dictionary
# 7.1. pop() and del() method removes the item with specificed key name
user_1.pop('gmail')
del user_1['company']
print('Print the user_1 dictionary after remove the item witk email and company keys: ', user_1)

# 7.2. If you want to remove the last item in dictionary and don't need to give a specificed key name
# you can use the popitem() method
user_1.popitem()
print('Print the user_1 dictionary after remove the last item: ', user_1)

# 7.3. Clear all data in the dictionary
user_1.clear()
print('Print the user_1 dictionary after clear all items: ', user_1)


# 7.3. Delete the dictionary
# this statement using user_1 variable (after delete statement execute) will be throw an exception
# the exception is the variable was not defined
del user_1
# print('Print the user_1 dictionary after delete user_1 ', user_1)
