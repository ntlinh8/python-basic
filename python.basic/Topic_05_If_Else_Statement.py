# Ex1
a = int(input('Enter value of a '))
if a % 2 == 0:
    print('a is even')
else:
    print('a is odd')

# Ex2
a = int(input('Enter value of a '))
b = int(input('Enter value of b '))
if a >= b :
    print('a is greater than or equal to b')
else:
    print('a smaller than b')

# Ex3
a = input('Enter value of name1 ')
b = input('Enter value of name2 ')
if a == b :
    print('Their names are the same')
else:
    print('Their names are NOT the same')

# Ex4
a = int(input('Enter value of a '))
if 22 <= a <= 65:
    print('a is in the range')
else:
    print('a is NOT in the range')

# Ex5
a = int(input('Enter the point of the student '))
if 0 < a < 4:
    print('Rate is D')
elif 4 <= a < 6:
    print('Rate is C')
elif 6 <= a < 8:
    print('Rate is B')
elif 8 <= a < 10:
    print('Rate is A')
else:
    print('You entered invalid number')