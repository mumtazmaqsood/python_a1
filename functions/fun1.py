

# defining function
def greet_user():
    print("Hello")

greet_user()

#passing arg to function
#name is the parameter
def greet_user1(name):
    print(f"Hello {name}!")

#argument
greet_user1('Mumtaz')

#positional arguments --> each argument match with the each parameter defined in the function definition
#keyword arguments --> write argument description
def describle_pet(animal_type = 'hamster', pet_name = 'harry'):
    """ Display information about a pet"""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describle_pet('Dog', 'jack')
describle_pet('test')


#TRY IT YOURSELF
#8-3 T-Shirt
def make_shirt(size = 'medium', msg = 'your message'):
    if size == 'medium' or size == 'large':
        print(f"Shirt Size: {size} & Message printed on Shirt: 'I love Python'")
    else:
        print(f"Shirt Size: {size} & Message printed on Shirt: {msg}")
make_shirt('any size', 'infinity')



















