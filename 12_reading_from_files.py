# in programs we often have to read information that was saved in files
# when you start your e-book reader, it looks up what page you were on when you last shut down
# when you start up your game, it looks up what treasures you had already collected so you can
# pick up where you left off
# there are also thousands of interesting open_data files out there you can read to find out cool
# information you can use in your programs.
# for example: you can find out what fauna they have at the museum in tasmania
# you would be amazed at the data files you can find on the internet

# ---------------------------------------------- #

# how do we read a file with code?
# use the open function
print("(1)")
my_file = open("extra/12_tasmania.txt", "r")

# how do we read the file contents?
# use the read method
file_content = my_file.read()
print(file_content)
# as you can see, the read method returns the entire content of the file into one big string

# don't forget to always close the file
my_file.close()

# ---------------------------------------------- #

print("(2)")
my_file = open("extra/12_tasmania.txt", "r")

# if you prefer you can read one line at a time
# use the read line method
file_content = my_file.readline()
print(file_content)

file_content = my_file.readline()
print(file_content)

# don't forget to always close the file
my_file.close()

# ---------------------------------------------- #

# if you're reading a csv file, there is a csv library that will help you
# to access the features in the csv library you must import it
# import csv

# now you can use the reader function to return all the rows from the file into a list
# data_from_file = csv.reader(my_file)

# if your file is not using a comma to separate the values, you can tell the reader function
# what character is used as a delimiter
# data_from_file = csv.reader(my_file, delimiter=";")

# now we can open and read a csv

import csv

print("(3)")
with open("extra/12_tasmania.txt", "r") as my_file:
    # read the file contents
    rows = csv.reader(my_file, delimiter=";")

    # why do we have a "with" and "as"
    # programs should always open a file, and close it when they are done
    # once we have all the rows from a csv files returned, how do we access the individual rows?
    # data_from_file is a list, so you can do all this we saw on the chapter about lists
    for row in rows:
        print(row)

        # but i don't like those square brackets and quotes it added to the rows!
        # you can use the join function to format the output
        # - SeparatorToDisplay.join(row)
        print(";".join(row))

        # what if i want to access an individual value from a row and not just print the whole row?
        # the row returned in the loop is actually a list of the words in that row
        # so you can just create a nested loop to loop through the words in the row
        for column in row:
            print(column)

# your challenge
# write a program that will print the names and ages of the guests in the guest list file you created in the last module
# if you didn't do the last challenge, you can just create a file to read using notepad that contains names and ages

print("(challenge)")
with open("extra/11_challenge.csv", "r") as my_file:
    rows = csv.reader(my_file, delimiter=";")

    for row in rows:
        print(";".join(row))

        for column in row:
            print(column)
