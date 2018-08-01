# if i want to know how many days until my birthday, first i need to know today's date
# the datetime class allows us to get the current date and time
# the import statement gives us access to the functionality of the datetime class
import datetime

# store the value in a variable called today
today = datetime.date.today()

print(today)

print(today.year)
print(today.month)
print(today.day)

print("{0:04d}".format(today.year))
print("{0:02d}".format(today.month))
print("{0:02d}".format(today.day))

# in python we use strftime to format dates
current = datetime.date.today()
# strftime allows you to specify the date format
print(current.strftime("%d/%m/%Y"))

# here's a few more oy may find useful
# %b is the month abbreviation
# %B is the full month name
# %y is the two digit year
# %Y is the four digit year
# %a is the day of the week abbreviated
# %A is the day of the week
# for a full list, check strftime.org

print(current.strftime("%d %b, %y"))
print(current.strftime("%d %B %Y"))

# could you print out a wedding invitation?
# please attend our event Sunday, July 20 in the year 1997

print(current.strftime("Please attend our event %A, %B %d in the year %Y"))

# localization in python: http://babel.pocoo.org/

# let's get back to calculating days until your birthday
# i need to ask your birthday
birthday = input("What's your birthday? (dd/mm/yyyy) ")
print("Your birthday is " + birthday)

# the strptime function allows you to convert a string to a date
birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y").date()

# why did we list datetime twice?
# because we are calling the strptime function
# which is part of the datetime class
# which is in the datetime module
print("Your birth month is " + birthday.strftime("%B"))

# what if the user fills a date in a different format?
# the program is going to crash
# you can tell the user the format you are expecting
# and you can try to handle the error, in case it occurs

# dates seem like a lot of hassle, is it worth it?
# why not just store them as strings?

# you can create a countdown to say how many days until a big event or holiday

next_birthday = datetime.datetime.strptime("03/06/2019", "%d/%m/%Y").date()
current_date = datetime.date.today()

# if you subtract two dates you get back the number of days between those dates
difference = next_birthday - current_date
print(difference.days)

# there's the module python-dateutil
# you can use it
# there's a lot of interesting functions


# and what about times?
# this module is called datetime, so yes, it can store times

current_time = datetime.datetime.now()
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# just like dates you can use strftime() to format the way a time is displayed

print(current_time.strftime("%H:%M %p"))

# %H hours (24hr clock)
# %l hours (12hr clock)
# %p AM or PM
# %m minutes
# %S seconds

# Challenge
# ask a user to enter the deadline for their project
# tell them how many days they have to complete the project
# for extra credit, give them the answer as combination of weeks and days
# hint: you will need some of the math functions from the module on numeric values

deadline = input("What's the deadline for this project? ")
try:
    d_deadline = datetime.datetime.strptime(deadline, "%d/%m/%Y")
    d_today = datetime.datetime.today()

    print("So, today it's {0} and you want this project for {1}"
          .format(d_today.strftime("%d/%m/%Y"), d_deadline.strftime("%d/%m/%Y")))

    n_days_between = d_deadline - d_today

    print("So we're talking about {0:d} days to deliver the project".format(n_days_between.days))

    n_weeks_between = int(n_days_between.days / 7)
    n_days_between = n_days_between.days - (n_weeks_between * 7)

    print("Or, even better, {0} weeks and {1} days. OK?".format(n_weeks_between, n_days_between))
except Exception as e:
    print("Sorry, but that is not a valid date, mate.")
