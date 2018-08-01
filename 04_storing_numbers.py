# It's important to be able to store and manipulate numbers as well as strings
age = 42
print(age)

# you can perform math operations on numeric values or on variables containing numeric values
width = 20
height = 5

area = width * height
print("Area of the rectangle: {0}".format(area))

# both ways are the same
perimeter = 2 * width + 2 * height
print("Perimeter of the rectangle: {0}".format(perimeter))

perimeter = 2 * (width + height)
print("Perimeter of the rectangle: {0}".format(perimeter))

# these are the most common math operations
# + addition 5 + 2 = 7
# - subtraction 5 - 2 = 3
# * multiplication 5 * 2 = 10
# / division 5 / 2 = 2.5
# ** exponent 5 ** 2 = 25
# % modulo 5 % 2 = 1

# math rules haven't changes since school
# order of operations
# () parenthesis
# ** exponent (e.g. **2 squared **3 cubed)
# /* multiplication and division
# +- addition and subtraction

area = 0
height = 10
width = 20

# calculate the area of a triangle
area = height * width / 2

print("Area of the triangle: {0}".format(area))


# sometimes you will need to format the numbers when you display them to users

# I have 6 cats (just converting that number into a string)
print("I have %d cats" % 6)
# I have   6 cats (formatted as integer with padding spaces to the left to make for 3 digits)
print("I have %3d cats" % 6)
# I have 006 cats (formatted as integer with padding zeros to the left to make for 3 digits)
print("I have %03d cats" % 6)
# I have 6.000000 cats (formatted as float with default cases)
print("I have %f cats" % 6)
# I have 6.00 cats (formatted as float with 2 decimal cases)
print("I have %.2f cats" % 6)

# you can also use a format method to format numeric values

# I have 6 cats (just converting that number into a string)
print("I have {0:d} cats".format(6))
# I have   6 cats (formatted as integer with padding spaces to the left to make for 3 digits)
print("I have {0:3d} cats".format(6))
# I have 006 cats (formatted as integer with padding zeros to the left to make for 3 digits)
print("I have {0:03d} cats".format(6))
# I have 6.000000 cats (formatted as float with default cases)
print("I have {0:f} cats".format(6))
# I have 6.00 cats (formatted as float with 2 decimal cases)
print("I have {0:.2f} cats".format(6))

# and here is another way of doing the same thing
print("Here are three numbers: %.2f, %.3f and %.4f" % (1, 2, 3))
# and here is another way of doing the same thing
print("Here are three numbers: {0:.2f}, {1:.3f} and {2:.4f}".format(1, 2, 3))


# sometimes commands are too long to fit on a single line
# you can use a "\" to indicate a command continues on the next line
total = 5 + 6 + 8 + \
        3 + 2

print(total)


# ask user for numeric input
str_idade = input("How old are you? ")
int_idade = int(str_idade)

print(int_idade + 1)


salary = input("Please enter your salary: ")
bonus = input("Please enter your bonus: ")

take_home_pay = salary + bonus

print(take_home_pay)


# there are functions to convert from one datatype to another:
# int(value) converts to an integer
# long(value) converts to a long integer
# float(value) converts to a number that can hold decimal places
# str(value) converts to a string

salary = input("Please enter your salary: ")
bonus = input("Please enter your bonus: ")

take_home_pay = float(salary) + float(bonus)

print(take_home_pay)

# what do you think will happen if someone types "BOB" as their salary?
# it's gonna crash
# we're gonna learn how to handle with errors later in the course


# your challenge - create a loan calculator
# have the user enter the cost of the loan, the interest rate, and the number of years for the loan
# calculate monthly payments with the following formula:
# M = L[i(1+i)n] / [(1+i)n-1]
# M = monthly payment
# L = loan amount
# i = interest rate(for an interest rate of 5%, i=0.05)
# n = number of payments
str_loan = input("Loan you want: ")
str_interest = input("Interest rate: ")
str_years = input("Number of years: ")

num_loan = float(str_loan)
num_interest = float(str_interest)
num_years = float(str_years)

num_payment = num_loan * (num_interest * (1 + num_interest) * num_years) / (((1 + num_interest) * num_years) - 1)

print("So, the monthly payment would be US$ {0:.2f}".format(num_payment))
