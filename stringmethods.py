course = 'Python for Beginners'
print (len (course) ) # both are functions len function is counting and forcing the number of chars or the length
course.upper() # method

print (course.upper ())
print (course.lower())
print (course)

#=============================
#=============================

course = 'Python for Beginners'
print (course.find('P'))
print (course.find('o'))
print (course.find('O')) # will be shown as -1 in the response since its not in the string
print (course.find ('Beginners')) # shown in the response as 11 since it starts at 11 char in the string

print (course.replace ('Beginners' , 'Absolute'))
print (course.replace ('B' , 'D'))
print (course.replace ('e' , '333'))

print ('Python' in course) # boolean - returns true
print ('python' in course) # boolean - returns false - since key sensative

#=============================
#=============================

course = 'Python for Beginners' # Define var as a Srting
len () #Function
course.upper() #Method for converting to upper case
course.lower() #Method
course.title() #Method
course.find() #Method
course.replace() #Method
'...' in course #chars in a string
