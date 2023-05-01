# assign operator
a = 5
a += 4
a *= 3

# math operator 
print(a + 4)
print(a - 4)
print(a * 4)
print(a / 4)
print(a % 4)
print(a ** 4)

# relation operator
print(a > 3)
print(a < 3)
print(a == 3)
print(a != 3)
print(a >= 3)
print(a <= 3)

# logic operator
print(a > 3 and a < 10)
print(a % 3 == 0 or a % 2 == 0)
print(not a > 5)

################### Exercise ###################
# Ex1
name = input('Please enter your name? ')
age = int(input('Please enter your age, {} '.format(name)))
print('After 10 years, the age of {} is {}'.format(name, age + 10))

# Ex2
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
x = x + y 
y = x - y
x = x - y
print(x)
print(y)

# Ex 3
a = int(input('Enter value of a '))
b = int(input('Enter value of b '))
print(a > b)
