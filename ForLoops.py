# for loop
#Example 1
for letter in "Python":
    print (letter)



#Example 2
for item in ['Artem', 'Andrey', 'Dasha', 'Larisa']: #in [ .. ] brackets defined list of items
    print (item)


#Example 3
for item in [1,2,3,4,5,6]: #in [ .. ] brackets defined list of items
    print (item)


#Example 4
for item in range (10): # RANGE FUNCTION - this is to define the range from 1 to 10
    print (item)


#Example 5
for item in range (5, 10): #this is to define the range from 5 to 10
    print (item)


#Example 6
for item in range (5, 10, 2): #this is to define the range from 5 to 10 with step in 2 digits
    print (item)


#Example 7
prices = [10,20,30]
total = 0
for item in prices:
   total = total + item
print (f"Total: {total}")