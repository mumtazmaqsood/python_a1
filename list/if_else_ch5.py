import random

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())



#check item is in list or not
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("mushrooms are in list")

#not in list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a comment")


#TRY IT YOURSELF

#5-1 Conditional Tests:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#if elif else --> as soon as one conditon true it ends but when need to check all conditions then use if
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#same program with if elif
print("-----------------------------------------")
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


#TRY IT YOURSELF
#5-3 Alien Colors
alien_color = 'green1'
if alien_color == 'green':
    print("you just earned 5 pt")
elif alien_color == 'yellow':
    print("you just earned 10 pt")
elif alien_color == 'red':
    print("you just earned 15 pt")
else:
    print("you earned zero pt")


#5-6 stages of life
age = 2
if age == 2:
    print("the person is a toddler")
elif age >= 4 and age < 13:
    print("The person is a Kid")
elif age >= 13 and age < 20:
    print("The person is teenager")
elif age > 19 and age < 65:
    print("the person is adult")
else:
    print("person is a elder")


#5-7 favorite fruit

favorite_fruits = ['blueberries', 'salmonberries', 'peaches']
if 'bananas' in favorite_fruits:
    print("you really like it")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")


#looping
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry {requested_topping} is out of stock !")
    else:
        print(f"Adding {requested_topping}")

#checking that a list is not empty

requested_toppings1 = ['a']
if requested_toppings1:
    for requested_topping in requested_toppings1:
        print(f"Adding {requested_topping}")
        print("Finished making pizza")
else:
    print("Are you sure! you want plain pizza")


# checking in multiple lists
print("Checking in mulitple lists")
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings2 = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings2:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry! we don't have {requested_topping} ")
print("Finished")




#TRY IT YOURSELF
#5-9,10Hello Admin,

usernames = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'admin']
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}! would you like to see a status report")
        else:
            print(f"Hello {username}, Thank you fro loggin in again")

else:
    print("We need to find some users!")

#5-10 checking username
current_users = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'admin']
new_users = ['k', 'l', 'm', 'n', 'o', 'p', 'g', 'admin']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}! need to enter a new username")
    else:
        print(f"{new_user}! is available")




#Assignment take input by user to add string
# no = 0
# i = 1
# user_input = input("Enter your number(0000):")
# for i in range(len(user_input)):
#   no = no + int(user_input[i])
# print(f"sum of total no:{no}")





from random import randrange
random_nos = random.randrange(1,10)
print(f"\n random nos guss")
print(random_nos)

while True:
    guss_no = int(input("guss a number:"))
    if guss_no == random_nos:
        print(f" You win: no is correct :{guss_no}")
        break
    elif guss_no > random_nos:
        print("your guss no is higher that the actual no")
    elif guss_no < random_nos:
        print("your guss no is lower that the actual no")


























