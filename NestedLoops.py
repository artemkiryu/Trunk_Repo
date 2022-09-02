for x in range (4):
    for y in range (3):
        print (f"({x}, {y})")

# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# (2, 1)
# (2, 2)
# (3, 0)
# (3, 1)
# (3, 2)

#================================

numbers = [5,2,5,2,2]
for item in numbers:
    output = ''
    for count in range(item):
        output += 'x'
    print (output)


numbers = [2,2,2,2,7]
for item in numbers:
    output = ''
    for count in range(item):
        output += 'x'
    print (output)