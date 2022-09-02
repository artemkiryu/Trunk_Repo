numbers = [5,2,1,7,4]
numbers.append(20) #add 20 at the end
print (numbers)

numbers = [5,2,1,7,4]
numbers.insert(0,10) #add 10 in front because we specify 0 as placemet
print (numbers)

numbers = [5,2,1,7,4]
numbers.remove(7) #removing 7
print (numbers)

numbers = [5,2,1,7,4]
numbers.clear() #clear ALL
print (numbers)

numbers = [5,2,1,7,4]
numbers.pop() # removes last number from the list
print (numbers)

numbers = [5,2,1,7,4]
print (numbers.index (5)) #will return index on where 5 is in the list

numbers = [5,2,1,7,4]
print (60 in numbers) #will return True or False in the response

#numbers = [5,2,1,7,4]
#print (numbers.index (60)) #will return Error that the number is not in the list

numbers = [5,5,5,2,1,7,4]
print (numbers.count (5)) #will return the count for how many 5s are in the list

numbers = [5,5,5,2,1,7,4]
numbers.sort() # will sort your list and return sorted list // [1, 2, 4, 5, 5, 5, 7]
print (numbers)

numbers = [5,5,5,2,1,7,4]
numbers.sort() # will sort your list
numbers.reverse() #will print reverced list // [7, 5, 5, 5, 4, 2, 1]
print (numbers)

numbers = [5,5,5,2,1,7,4]
numbers2 = numbers.copy()
numbers.append(10) # add 10 the the first list while copy of the list is still original
print (numbers)
print (numbers2)


numbers = [5,5,5,2,1,7,4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append (number)
print (uniques)
