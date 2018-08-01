def your_name_as_james_bond(first_name, last_name):
    return "{1}, {0} {1}".format(first_name, last_name)


# the input function allows you to specify a message to display and returns the value typed in by the user
# we use a variable to remember the value entered by the user
# we called our variable "first", but you can call it just about anything as long it doesn't contain spaces
fst_name = input("What's your first name? ")
snd_name = input("What's your last name? ")

# You can combine variables and string with the "+" symbol
print("So, your name is " + your_name_as_james_bond(fst_name, snd_name))


# That's another way of doing it
# This way you print the message and then as for user response in another line
print("What's your first name?")
fst_name = input()
print("What's your last name?")
snd_name = input()
print("So, your name is " + your_name_as_james_bond(fst_name, snd_name))


# This way is much much more awesome
fst_name = input("First name.....: ")
snd_name = input("Last name......: ")

print("So, your name is " + your_name_as_james_bond(fst_name, snd_name))


# variables cannot contains spaces
# variables are case sensitive (firstname e firstName would be two different names)
# variables cannot start with numbers
# variables should be descriptive but not too long (favoriteSign not yourFavoriteSignInTheHoroscope)
# use a casing scheme: camelCasing or PascalCasing or spacing_casing

# Variable1 <-- wrong, not very descriptive
# First Name <-- wrong, it has a space in the middle
# Date <-- wrong, reserved word
# 3Name <-- wrong, starts with number
# DOB <-- king of ok, should be more descriptive
# DateOfBirth <-- perfect
# YourFavoriteSignInTheHoroscope <-- wrong, too long


# variables also allow you to manipulate the contents of the variable:
# lower, upper and swapcase are different string functions
message = "Hello World!"
print(message.lower())
print(message.upper())
print(message.swapcase())


# what do you think there functions will do?
message = "Hello world!"
# starts with 0
print(message.find("world"))
# how many times you see an "o" within the content of the string
print(message.count("o"))
# capitalize() capitalizes the first letter
print(message.capitalize())
# swapping Hello by Hi
print(message.replace("Hello", "Hi"))


# programmers don't memorize all these functions!!!
# so how do programmers find them when they need them?
# intellisense (ctrl + space)
# documentation
# internet searches


# how could we have a user enter their postal code and then display that
# postal code in upper case letters even if the user typed it in lower case?
postal_code = input("What is your postal code number?")
postal_code = postal_code.upper()

print("Ok, so you mean it is {0}".format(postal_code))


# functions and variables allow us to make new mistakes in our code:
# each line of code below has a mistake
# message = Hello world <-- where are the quotes?
# 23message = "Hello world" <-- variables must not start with numbers
# New message = "Hello world" <-- variables must not have spaces
# print(message.upper) <-- upper() is a string function, and all functions need parenthesis
# print(mesage.lower()) <-- there's a typo in "message"
# print(message.count()) <-- you should have specified the parameter


# Challenge
# Write a program that allows a person to personalize a story
# Take a page from a book or make up a story.
# Ask the user to enter information you can replace in the story such as their name, a place, or insert
# adjectives or adverbs into the story.
# Then display the personalized story to the user.
content = input("Send me the content of your book: ")
name = input("What is the name of the main character? ")
place = input("Where does he live? ")

changed_text = content.replace(name, "Allan Poe").replace(place, "Edinburgh")

print(changed_text)
