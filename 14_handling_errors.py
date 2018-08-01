# syntax errors are errors that the development tool can detect
# but sometimes typing mistakes can't be detected until you run the program

# logic errors are syntactically correct, but the program doesn't do what we want it to do
salary = "5000"
bonus = "500"
paycheck = salary + bonus
print(paycheck)

# runtime errors occur when the code basically works but something out of the ordinary crashes the code
# you write a calculator program and a user tries to divide a number by zero
# your program tries to read a file, and the file is missing
# your program is trying to perform a date calculation and the date provided is in the wrong format

# having your code crash is a very poor experience for the user

# let's create a calculator program that will take two numbers and divide them for the user
first = input("Enter the first number: ")
second = input("Enter the second number: ")

first_number = float(first)
second_number = float(second)

try:
    result = first_number / second_number
    print("{0:.2f} / {1:.2f} = {2:.2f}".format(first_number, second_number, result))
except:
    print("Sorry, but something went wrong")
finally:
    print("I will always run. I'm useful for close the the database or text file")
    print("It is gaaranteed that it will run, even if you run a sys.exit()")

# now try to divide by zero
# a-ha! it crashed
# ZeroDivisionError: float division by zero

# you can add try/except around the code that generates the error to handle it gracefully

# if you want to know what the error was, you can use the function sys.exc_info()
import sys

first_number = 3
second_number = 0

try:
    result = first_number / second_number
    print("{0:.2f} / {1:.2f} = {2:.2f}".format(first_number, second_number, result))
except:
    error = sys.exc_info()[0]
    print("Sorry, but something went wrong")
    print(error)

# after you got the name of the error, you might show the user a specific messagem
first_number = 3
second_number = 0

try:
    result = first_number / second_number
    print("{0:.2f} / {1:.2f} = {2:.2f}".format(first_number, second_number, result))
except ZeroDivisionError:
    print("Sorry, but you can't divide by zero")

# how can i force my program to exit if an error occurs and i don't want to continue?
# you can use the function sys.exit() in the sys library
try:
    result = first_number / second_number
    print("{0:.2f} / {1:.2f} = {2:.2f}".format(first_number, second_number, result))
except ZeroDivisionError:
    print("Sorry, but you can't divide by zero")
    # sys.exit()
print("Hey! I'll never run!")

# you can also use variables and an if statement to control what happens after an error
error = False
try:
    result = first_number / second_number
    error = False
except ZeroDivisionError:
    error = True

if not error:
    print("{0:.2f} / {1:.2f} = {2:.2f}".format(first_number, second_number, result))

# there are a lot of different situations that can raise errors in our code
# converting between data types
# opening files
# mathematical calculations
# trying to access a value in a list that does not exist

# how do you know what errors will be raised?
# you can test it yourself and when an error occurs use the sys.exc_info() function to get the name of the error

# but the most important thing to do is test!
# 1. execute your code with everything running normally
# 2. execute your code with incorrect user input
#   - enter letters instead of numbers
#   - enter 0 or spaces
#   - enter a value in the wrong format (e.g. dates)
# 3. try other error scenarios such as missing files
# 4. try anything you can think of that might crash your code
#   - entering really big numbers
#   - negative numbers

# do i need to handle every possible error?
# - sometimes writing the code to handle the errors takes more time than writing the original program
# - whether it is necessary to handle every possible error depends on how the code will be used
# - if you are writing a system for air traffic control i would want very thorough error handling

# your challenge
# write code to open and read a file
# allow the user to specify the file name
# add error handling to provide a suitable error message if the file specified by the user could not be found
path_name = "extra/"
file_name = input("Type the name of the file you want to read: ")

try:
    my_file = open(path_name + file_name, "r")
    print(my_file.read())
    my_file.close()
except FileNotFoundError as e:
    print("File not found!")
