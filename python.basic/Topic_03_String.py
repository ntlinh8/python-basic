test = "Nguyen Thuy Linh"

isExist = 'Linh' in test
print('Linh exist in the test: ' + str(isExist))

# Co the thay khi dung ham .upper() thi se khoi tao mot vung nho moi chu ko su dung vung nho cua test variable nua
print('Upper of str: ' + test.upper())
print('Test is ' + test)

print('Lower of str: ' + test.lower())
print('Test is ' + test)

# Tach chuoi va tra ve mot mang array chua cac phan tu thu duoc
arrList = test.split(' ')
print(arrList)
print(arrList[1])

#Casting
i = 12

# Ep kieu tuong minh
print("Print 2 data type" + test + str(i) )

# Ep kieu ngam dinh
sum = i + 5.2
print(float(i))

# Get substring - tu index i = 0, i < 2
# cach 1
print(test[0:2])

# cach 2
address = 'AUTOMATION'
# Get char at index = 1 to 5 -> UTOM
# Jum 3 buoc -> lay ra M
S1 = slice(1, 5, 6)
print(address[S1])

