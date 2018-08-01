import turtle

# sometimes we need to perform an action more than once
# pour a cup of coffee for each guest
# wash the dishes until they are all clean
# make a name card for each guest attending a party

# for loops allow us to execute code a fixed number of times
# so if we know there are twenty guests we can print twenty name cards
for guest in range(20):
    print(guest)

# while loops allow you to execute until a particular condition is true
answer = "0"
while answer != "4":
    answer = input("How much is 2 + 2? ")

print("Yes! 2 + 2 = 4!")

# can you figure out what this code will do?
counter = 0
while counter < 4:
    turtle.forward(100)
    turtle.right(90)
    counter = counter + 1

# what happens if you forget to increment the counter?
# an infinite loop!
# be extra careful when you use while
# it is all on your control!

# it's easier to make a mistake with a while loop than a for loop
# use for loops whenever possible
# but don't fear the while loop

# your challenge
# create and etch a sketch program
# have the user enter a pen color, a line length, and an angle
# use turtle to draw a line based on their specifications
# let them specify new lines over and over until they enter a line length of 0
turtle.clearscreen()
line_length = 1
while line_length != 0:
    pen_color = input("What's the pen color you want for this particular sketch? ")
    line_length = input("What's the line length you want for this particular sketch? ")
    angle = input("What's the angle you want to draw this particular sketch? ")
    turtle.color(pen_color)
    turtle.forward(int(line_length))
    turtle.right(int(angle))
