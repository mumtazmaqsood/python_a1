#
#
# #counting numbers
# no = 1
# while no <= 5:
#     #print(no)
#     no += 1
#
#
# # while loop --> while user write quit then program end
# # prompt = "\nTell me something, and I will repeat it back to you:"
# # prompt += "\nEnter 'quit' to end the program. "
# # message = ""
# # while message != 'quit':
# #     message = input(prompt)
# #     print(message)
# #----------------------------------------------
#
# #above program with Flag
# # prompt = "\nTell me something, and I will repeat it back to you:"
# # prompt += "\nEnter 'quit' to end the program. "
# # message = ""
# # active = True
# # while active:
# #     message = input(prompt)
# #     if message == 'quit':
# #         active = False
# #     else:
# #         print(message)
#
# #continue statment
# current_no = 0
# while current_no < 10:
#     current_no += 1
#     if current_no % 2 == 0:
#         #break
#         continue
#
#     print(current_no)
#
#
#
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"verifying users: {current_user.title()}")
#     confirmed_users.append(current_user)
# #Display all confirmed users
# for user in confirmed_users:
#     print(f"Confirmed Users: {user}")
#
#
# #Removing specific values in the list using remove() method
#
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(f"Pets list:{pets}")
# while 'cat' in pets:
#     pets.remove('cat')
# print(f"Latest Pets list: {pets}")
#
# # Filling Dic with users Input
#
# # user_response = {}
# # polling_status = True
# #
# # while polling_status:
# #     name = input("Enter your name:")
# #     response = input("Whcih mountain would you like to climb someday?")
# #     user_response[name] = response
# #     repeat = input("Would you like to let another person respond? (yes/no):")
# #     if repeat == 'no':
# #         polling_status = False
# #
# # print(f"dic:{user_response}")
# # print(f"\n--------Polling Reults-----")
# # for name, response in user_response.items():
# #     print(f"{name} would like to climb {response}.")
#
# #TRY IT YOURSELF
#
# #7-8 Deli
# sandwich_order = ['veg', 'pastrami','fish','pastrami', 'meat', 'pastrami']
# finished_sandwich = []
#
# print(" Sorry pastrami! sandwich has been finished")
#
# while 'pastrami' in sandwich_order:
#    sandwich_order.remove('pastrami')
#
# print(f"updated sandwich orders: {sandwich_order}")
#
# while sandwich_order:
#     current_sandwich = sandwich_order.pop()
#     print(f"I made your {current_sandwich} sandwich")
#     finished_sandwich.append(current_sandwich)
# #
# print(f"finisnhed sandwich: {finished_sandwich}")
# for order in finished_sandwich:
#     print(f"your sandwich {order} is ready!")
#
#
#
#
#
# #7-10 Dream Vacation
#
# # dream_vocations = {}
# # flag = True
# # while flag:
# #     user_name = input("Enter your name:")
# #     location = input("If you could visit one place in the world, where would you go?")
# #     dream_vocations[user_name] = location
# #     repeat = input("Would you like to repeat?(yes/no)")
# #     if repeat == 'no':
# #         flag = False
# # print(f"DreamVocations:{dream_vocations}")
# # for name, vocation in dream_vocations.items():
# #     print(f"{name}: {vocation}")
#
#
#
#
# #ask user to input a number containing more than one digit
# # 1235 > 1 +2+3+5 = 11
# sum = 0
# nos = input("Enter number to add:")
# for no in range(len(nos)):
#     sum = sum + int(nos[no])
# print(sum)
#
# #ask a user for name and print count of each word
#
# user_name = input("Enter your name:")
# i = 0
# temp_var = ""
# while i < len(user_name):
#     if user_name[i] not in temp_var:
#         temp_var += user_name[i]
#         print(f"{user_name[i]}: {user_name.count(user_name[i])} ")
#     i += 1



# sum of 1 to 10
# sum = 0
# for i in range(1,5):
#     sum += i
# print(sum)


# sum of 1 - n number
# sum_no = int(input("Enter your desired no to sum."))
# sum = 0
# for i in range(1, sum_no + 1):
#     sum += i
# print(sum)

for i in range(5):
    print(i)




































