
#Returning list

def greet_user(user_names):
    for name in user_names:
        msg = f"Hello, {name.title()}"
        print(msg)
names = ['a', 'b', 'c']
greet_user(names)


#list printing example
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     printed = unprinted_designs.pop()
#     print(f"printing model: {printed}")
#     completed_models.append(printed)
# for printed_model in completed_models:
#     print(f"completed_model: {printed_model}")

#above example with function

def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        printed = unprinted_designs.pop()
        print(f"printing model: {printed}")
        completed_models.append(printed)

def show_completed_models(completed_models):
    for printed_model in completed_models:
        print(f"completed_model: {printed_model}")

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
#unprinted_designs[:] will pass the copy of the list -- if this syntax is not used then all data will be earsed and empty list printed
#
print_model(unprinted_designs[:], completed_models)
if "iphone case" in completed_models:
    completed_models.remove("iphone case")
show_completed_models(completed_models)
print(f"unprinted_designs: {unprinted_designs}")
print(f"completed_model: {completed_models}")

#TRY IT YOURSELF
#8-9
message_list = ["hello there", "how are u?", ":-)"]
sent_messages = []
def messages(msg):
    print("Showing all messages:")
    for text in msg:
        print(text)


def sending_message(msg, sent_msg):
    print("Sending all messages...")
    while msg:
        get_msg = msg.pop()
        print(get_msg)
        sent_msg.append(get_msg)

print("\n Final list")
messages(message_list)
sending_message(message_list[:], sent_messages)

print(f"Message_List:{message_list}")
