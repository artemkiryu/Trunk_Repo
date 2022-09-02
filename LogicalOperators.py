# Conditions and Logical operators


has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print ("Eligible for a loan.")
# The response is printed

print ("===========================")

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print ("Eligible for a loan.")
# The response is NOT printed

print ("===========================")

has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print ("Eligible for a loan.")
# The response is printed if one of the conditions is true

print ("===========================")

has_high_income = True
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print ("Eligible for a loan of $10,000.")
# The response is printed if one is true and second is false
