# if statements allow you to specify code that only executes if a specific condition is true

answer = input("Would you like express shipping for an extra $10? ")

if answer.lower() == "yes":
    print("All right!")
else:
    print("Ok, no problem")

# you can use different symbols to check for different conditions
# == is equal to                    if total == 1000:
# != is not equal to                if total != 1000:
# <  is less than                   if total < 1000:
# >  is greater than                if total > 1000:
# <= is less than or equal to       if total <= 1000:
# >= is greater than or equal to    if total >= 1000:

favorite_team = input("What is your favorite hockey team? ")

if favorite_team.lower() == "senators":
    print("Yeah Go Sans Go")
    print("But I miss Alfredsson")

print("It's ok if you prefer soccer/football")

# almost every if statement can be written two ways

# if answer == "yes" :
# if not answer == "no":

# if total < 100:
# if not total >= 100:

# what if we try an if statement with numbers instead of strings
str_deposit = input("How much do you want to deposit? ")
num_deposit = float(str_deposit)

# you could have also done like this:
# tmp_deposit = float(input("How much do you want to deposit? "))

if num_deposit > 100:
    print("You get a free toaster!")
else:
    print("Enjoy your mug!")

print("Have a nice day!")


# you can use boolean variables to remember if a condition is true or false
str_deposit = input("How much do you want to deposit? ")
num_deposit = float(str_deposit)
bol_toaster = False

if num_deposit > 100:
    bol_toaster = True

if bol_toaster:
    print("Enjoy your free toaster!")

# your challenge
# calculate shipping charges for a shopper
# ask the user to enter the amount for their total purchase
# if the amount is under $50 add $10, otherwise shipping is free
# tell the user their final total including shipping costs and format the number so it looks like a monetary value
# don't forget to test your solution with a value > 50, a value < 50 and a value of exactly 50

num_shipping_costs = 10
str_products_price = input("What's the total amount for the products you are buying? US$ ")
num_products_price = float(str_products_price)
if num_products_price >= 50 :
    num_shipping_costs = 0

num_total_purchase = num_products_price + num_shipping_costs
print("So, your total purchase with shipping included will set you off US$ {0:.2f}".format(num_total_purchase))
