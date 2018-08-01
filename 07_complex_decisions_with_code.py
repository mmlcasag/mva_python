# sometimes there are multiple conditions that affect the outcome of a decision
# if you are in england you say hello
# if you are in germany you say guten tag
# if you are in france you sei bonjour

# the elif allows you to check for different values
country = input("Where are you from? ")

if country.upper == "CANADA":
    print("Hello")
elif country.upper() == "GERMANY":
    print("Guten Tag")
elif country.upper() == "FRANCE":
    print("Bonjour")
else:
    print("Bom dia")

# what if you want to check two conditions?
# and
age = input("How old are you? ")
gender = input("What's your gender? ")

if float(age) > 18 and gender == "male":
    print("Alright, you can watch this video")
else:
    print("Sorry, you can't watch this video")

# possible combinations of and
# false and false = false
# false and true  = false
# true  and false = false
# true  and true  = true

# what if you want to check either of these conditions?
# or
age = input("How old are you? ")
gender = input("What's your gender? ")

if float(age) > 18 or gender == "male":
    print("Alright, you can play soccer")
else:
    print("Sorry, you can't play soccer")

# possible combinations of or
# false or false = false
# false or true  = true
# true  or false = true
# true  or true  = true

country = ""
pet = ""

# there is an order of operations for and/or:

# and is evaluated first
if country == "CANADA" and pet == "MOOSE" or pet == "HORSE":
    print("Do you play hockey too?")

# this would automatically do this
if (country == "CANADA" and pet == "MOOSE") or pet == "HORSE":
    print("Do you play hockey too?")

# you have to do this:
if country == "CANADA" and (pet == "MOOSE" or pet == "HORSE"):
    print("Do you play hockey too?")

# or you can also do this:
country_is_canada = False
if country == "CANADA":
    country_is_canada = True

pet_is_correct = False
if pet == "MOOSE" or pet == "HORSE":
    pet_is_correct = True

if country_is_canada and pet_is_correct:
    print("Do you play hockey too?")

# you can nest if statements inside each other

monday = True
fresh_coffee = False

if monday:
    # you could have code here to check for fresh coffee
    # the if statement is nested, so this if statement
    # is only executed if the other if statement is true
    if not fresh_coffee:
        print("Go buy a coffee!")
    print("I hate mondays!")
print("now you can start work")

# your challenge
# calculate the total to charge for an order from an online store in canada
# ask user what country they are from and their order total
# if the user is from canada, ask which province
# if the order is from outside of canada do not charge any taxes
# if the order was placed in canada, calculate tax based on the province
# - alberta = .05% general sales tax
# - ontario, new brunswich, nova scotia charge .13% harmonized sales tax
# - all other provinces charge .06% provincial sales tax + .05% GST tax

str_country = input("Which country are you from? ")
str_order = input("What is you order total? $ ")
num_order = float(str_order)

if str_country.upper() == "CANADA":
    str_province = input("Which province are you from? ")

    if str_province.upper() == "ALBERTA":
        # adding general sales tax
        num_order = num_order * 1.05
    elif str_province.upper() == "ONTARIO" or str_province.upper() == "NEW BRUNSWICH" or str_province.upper() == "NOVA SCOTIA":
        # adding harmonized sales tax
        num_order = num_order * 1.13
    else:
        # adding provincial sales tax
        num_order = num_order * 1.06
        # adding general sales tax
        num_order = num_order * 1.05

print("Your total order price is {0:.2f} $ ".format(num_order))
