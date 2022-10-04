

#function called within function is called clourse
#in decorators, function passed as argument to other function and need not to call that function
#decorator are the tags, it can be assigned to any function and decorator should have its definition

# def mydeco(func):
#     name = input("Enter your name")
#     print(func(name))
# @mydeco
# def greeting(name):
#     return f"Welcome {name}"
#
# #in above example, we are not calling funciton, it is executing autoamtically.
# @mydeco
# def not_welcome(name):
#     return f"{name}, you are not welecome"


#Another example

def profile_fetcher(func):
    name = "Mumtaz"
    age = 40
    profile = func(n=name, a=age)
    print(profile)
@profile_fetcher
def profile_builder(**details):
    profile = {}
    for k, v in details.items():
        profile[k] = v
    return profile














