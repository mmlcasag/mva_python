# you can create an empty list and add values later
guests = []
scores = []

# lists allow you to store multiple values
guests = ["Christopher", "Suzy", "Bill", "John"]
scores = [78, 85, 62, 49, 98]

# you can reference any value in the list by specifying its position in the list

# print the first guest - the first guest is in position 0
print(guests[0])
# print the fourth score - the fourth score is in position 3
print(scores[3])

# you can even count backwards

# print the last entry in the list
print(guests[-1])
# print the second last entry in the list
print(guests[-2])

# you can change a value in a list
print("First guest was " + guests[0])
guests[0] = "Michelle"
print("First guest is now " + guests[0])

# you can add a value to a list with append()
guests.append("Zyon")
guests.append("Olaf")
guests.append("Ozzy")
guests.append("Otta")
guests.append("Luca")

# you can remove a value from a list with remove()
guests.remove("Ozzy")

# you can also use the del command to delete an entry
del guests[0]

# the index() function will search the list and return the index of the position where the value was found
# this will return the index in the list where the name Olaf is found
print(guests.index("Olaf"))

# what do you think will happen if we search for a value that doesn't exist in the list?
# print(guests.index("Marietta"))
# ValueError: 'Marietta' is not in list

# you can use the len() function to find out how many entries are in your list
num_entries = len(guests)
print(num_entries)

print("--")

# looping through a list (the dumb way)
for guest in range(num_entries):
    print(guests[guest])

print("--")

# looping through a list (the smart way)
for guest in guests:
    print(guest)

print("--")

# you can sort your list with the sort() function
# sort the guests in alphabetical order
guests.sort()

# print again the list
for guest in guests:
    print(guest)

# your challenge
# ask the user to enter the names of everyone attending a party
# then return a list of the party guests in alphabetical order
# this will require pulling together everything we have learned so far, so let's walk through the thought process
# of idea to code

guests = []
guest = "Whatever"

while guest != "":
    guest = input("What's the name of the next guest? (or leave it empty to exit) ")
    guests.append(guest)

guests.sort()

for current_guest in guests:
    print(current_guest)
