names = ['John', 'Bob', 'Mosh', 'Sara', 'Mary']
print (names [2:])

names = ['John', 'Bob', 'Mosh', 'Sara', 'Mary']
print (names [2:4])

names = ['John', 'Bob', 'Mosh', 'Sara', 'Mary']
print (names [:]) # Returns all items from the list

names = ['John', 'Bob', 'Mosh', 'Sara', 'Mary']
names [0] = 'Jon' # To OVERWRITE name John to Jon
print (names [2:])
print (names)


numbers = [1,2,3,4,5,6,7,8,9,10]
print (numbers [-1])


numbers = [3,6,2,8,4,10]
max = numbers [0]
for number in numbers:
    if number > max:
        max = number
print (max)