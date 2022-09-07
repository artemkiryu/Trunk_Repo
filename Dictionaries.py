customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print (customer ["name"])
print (customer.get ("name"))
print (customer.get ("birthdate"))

customer ["school years"] = "6 years"
print (customer ["school years"])

#========================
# Program:
phone = input("Phone:")
digits_mapping = {
"1" : "One",
"2" : "Two",
"3" : "Three",
"4" : "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get (ch, "!") + " "
print (output)

