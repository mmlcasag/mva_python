import datetime

# repetition
# one of the problems with code is you're frequently doing the same thing over and over again
# - the same few lines of code
# - the same tasks
# - the same operations

# what is a function?
# - a reusable section of code with a name that does something
# - sometimes called a method

# you have already used functions!
# - print
# - open
# - write
# - close

# why create functions?
# - code reuse: you are doing the same thing over and over again
# - simplify: functions have names to define what they do
# - simplify: breakdown complex blocks of code
# - easier to make changes
# - if it's been written once, you only have to update it once

# how do we create a function?
# use the keyword def (short for define)
# give a name for your function
# write the code in the body of the function


def print_welcome():
    print("Hello World!")


# how do you call a function?
# - simply use its name
print_welcome()


def print_names(list):
    for name in list:
        print(name)
    return


# define this function
# when someone calls this function, execute this code
def main():
    names = ["Ragnar", "Bjorn", "Olaf"]
    # yes, you can call one function inside other function
    print_names(names)
    return


# execute the function
# in order to do that the function must be created
main()


# i'd like my function to be dynamic
# in our examples the functions we created only did one thing
# sometimes that's exactly what we need
# but sometimes we need some flexibility
# create custom messages to be displayed
# provide two numbers for a calculation
# print to the screen, and optionally, to a file

# what about parameters?
# they are nothing more than variables
# like in print, you are sending in a string as a parameter for the function print
def alert(text):
    print(text)
    return


# what about multiple parameters?
# simply add them in, separated by commas
def display_message(greeting, name):
    message = greeting + "," + name
    print(message)
    return


display_message("Hi", "Marcio")


# functions return data using the return keyword
# specify the value or data you want to pass back after the return keyword
# you can reuse names in different functions
def get_message(name):
    message = "Hello, " + name
    return message


def print_message(message):
    print(message)
    return


output = get_message("Christopher")
print_message(output)


# your challenge
# create a function to simplify writing to files
# set the function to accept parameters
# - one for text
# - one for the name of a file
# add the code that will write the text out to the file


def write_to_file(file_name, file_content):
    my_file = open(file_name, 'w')
    my_file.write(file_content)
    my_file.close()


def append_to_file(file_name, file_content):
    my_file = open(file_name, 'a')
    my_file.write(file_content + "\n")
    my_file.close()


file = "extra/13_challenge.txt"

write_to_file(file, "War for territory\nWar for territory\n")

append_to_file(file, "Years of fighting")
append_to_file(file, "Teaching my son")
append_to_file(file, "To believe in that man")

# extra challenge
# write a to_date() e to_char() function in the format you want


def to_date(date):
    return datetime.datetime.strptime(date, "%d/%m/%Y").date()


def to_char(date):
    return date.strftime("%d/%m/%Y")


dat_date = to_date("31/07/2018")
print(to_char(dat_date))
