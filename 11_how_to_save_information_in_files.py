# have you ever needed to jot something down to remember it later?
# a list of ingredients to buy for a recipe?
# a guest list?
# a phone number?

# sometimes even programs need to jot something down so they can remember it later
# remember what page i was reading my e-book
# remember what treasures i had collected when i took a break from the game

# working with files
# one of the ways a program can make a note of something it to write it to a file

# how do you write to file with code?
# use the open function to create and open a file
# my_file = open(file_name, access_mode)
# you must specify
# - file name
# - access_mode

# what is the name file?
# the file name is the name of your file including the extension (data.txt, my_times.csv)
# the file will be created in the same folder as your program

# what is the access mode?
# the access mode specifies what you will do with the file after you open it
# you can specify any of the following:
# - r: read the file
# - b: open a binary file
# - w: write to the file
# - a: append to the existing file content
# - w+: read and write at the same time
WRITE = "w"
file = open("extra/11_guest_list.txt", mode=WRITE)

# if the file doesn't exist, python will create it
# write is always going to overwrite the file
# append will add the content at the end of the file

# now that we have a file, how do we write to it?
# use the write function
file.write("Hi there!")
file.write("How are you?")
# as you can see, it wrote all on the same  line

# if you want to print in the next line, think about print statements
# remember \n?
file.write("\nHi there!")
file.write("\nHow are you?")

print("--------------------------")

file_name = "extra/11_demo.csv"
APPEND = "a"

file = open(file_name, mode=APPEND)

file.write("Name;Age;\n")
file.write("Susan;29;\n")
file.write("Christopher;31;\n")

print("--------------------------")

file_name = "extra/11_user_file.txt"
WRITE = "w"

data = input("Please enter file info: ")
file = open(file_name, mode=WRITE)
file.write(data)

print("Files written successfully")

# your challenge
# create the csv file below!

file = open("extra/11_challenge.csv", "w")

emp_name = " "
emp_age = "0"
while emp_name != "":
    emp_name = input("Please enter employee name: ")
    emp_age = input("Please enter employee age: ")

    file.write(emp_name + ";" + emp_age + ";" + "\n")

print("Files written successfully")

# when you are done you should always close the file
# use the close method
file.close()
