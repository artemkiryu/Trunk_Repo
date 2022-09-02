is_hot = True
if is_hot:
    print ("Its a hot day.")
print ("Enjoy your day!")

print ("==============================")

#if, else if, else statements

is_hot = True #boolian
is_cold = False #boolian
if is_hot:
    print ("Its a hot day.")
    print ("Drink lots of water.")
elif is_cold:
    print ("Its a cold day.")
    print ("Wear warm clothes.")
else:
    print ("Its a lovely day!")
print ("Enjoy your day!")

print ("==============================")

#Exercise

house_price = 1000000
good_credit = False
# bad_credit = False

if good_credit:
    print ("Put down 10%")
    print ("Down payment is 100000")
else:
    print ("Put down 20%")
    print ("Down payment is 200000")

print ("==============================")

#Exercise 2 // More logical solution

house_price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price
print (f"Down payment: ${down_payment}")

