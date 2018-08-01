import turtle

# in code, we use loops to repeat a task
# we are going to have some fun in this module by drawing objects
# we will use loops to draw some of our objects

# hello turtle

# turtle is a python library that lets you draw

# you can probably guess what some of the turtle commands do:
# right(x) --> rotate right x degrees
# left(x) --> rotate left x degrees
# color("x") --> change pen color to "x"
# forward(x) --> move forward x
# backward(x) --> move backward x

# how would we get turtle to draw a square?
turtle.clearscreen()
turtle.color("green")
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

# we are basically repeating those first 2 lines 4 times
# so we oculd just do this instead:
turtle.clearscreen()
turtle.color("blue")
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)

# only the indented code is repeated
turtle.clearscreen()
turtle.color("red")
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.forward(200)

# you can have lots of fun whn you put a loop inside another loop
turtle.clearscreen()
turtle.color("yellow")
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
    for more_steps in range(4):
        turtle.forward(50)
        turtle.right(90)

# just for fun
turtle.clearscreen()
turtle.color("purple")
for steps in range(5):
    turtle.forward(100)
    turtle.right(360 / 5)
    for more_steps in range(5):
        turtle.forward(50)
        turtle.right(360 / 5)

# you can also use a variable to decide the number of sides our object will have
turtle.clearscreen()
turtle.color("brown")
sides = 7
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360 / sides)
    for more_steps in range(5):
        turtle.forward(50)
        turtle.right(360 / sides)

# you can look at the loop values within the loop
for steps in range(4):
    print(steps)
# it starts with 0, so it's gonna print 0, 1, 2, 3 (4 times)

# if you need to start counting from "1" you can specify numbers to count to and from
for steps in range(1, 4):
    print(steps)
# it executes up until for, so it's gonna print 1, 2, 3 (3 times)

# you can also tell the loop to skip values by specifying a step
for steps in range(1, 10, 2):
    print(steps)
# it executes  from 1 up until 10, so it would print 1, 2, 3, 4, 5, 6, 7, 8, 9
# but since it increments 2 by 2, it would actually print 1, 3, 5, 7, 9

# one of the cool things about python is the way you can tell it exactly what values
# you want to use in the loop
for steps in [1, 2, 3, 4, 5]:
    print(steps)
# in this case, yes, it will execute for the last value
# so this would print 1, 2, 3, 4, 5

# and you don't have to use numbers!
turtle.clearscreen()
turtle.color("black")
for steps in ["red", "blue", "purple", "black"]:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)

# you can even mix up different data types, for example, numbers and strings, but it may raise some errors
for steps in ["red", "blue", "purple", "black", 8]:
    print(steps)

# Your challenge
# get turtle to draw an octagon
# hint: to calculate the angle, you take 360 degrees and divide it by the number of sides of the shape you are drawing.
# extra challenge: let the user specify how many sides the object will have and draw whatever they ask
# double bonus challenge: add a nested loop to draw a smaller version of the object inside

# regular challenge
turtle.clearscreen()
turtle.color("red")
sides = 8
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360 / sides)
    for more_steps in range(sides):
        turtle.forward(50)
        turtle.right(360 / sides)

# extra challenge
turtle.clearscreen()
turtle.color("orange")
sides = int(input("How many sides do you want? "))
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360 / sides)
    for more_steps in range(sides):
        turtle.forward(50)
        turtle.right(360 / sides)

# double bonus challenge
turtle.clearscreen()
turtle.color("blue")
sides = int(input("How many sides do you want? "))
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360 / sides)
    for more_steps in range(sides):
        turtle.forward(50)
        turtle.right(360 / sides)
        for even_more_steps in range(sides):
            turtle.forward(25)
            turtle.right(360 / sides)
