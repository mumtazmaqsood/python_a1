
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'tuna', 'sald', 'extra cheez')


#looping on above example
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\n Making the pizza with following topping:")
    for topping in toppings:
        print(topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'tuna', 'sald', 'extra cheez')

#positional arg
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print(f"\n pizza size: {size} with following topping:")
    for topping in toppings:
        print(topping)

make_pizza(12, 'pepperoni')
make_pizza(15, 'mushrooms', 'tuna', 'sald', 'extra cheez')



#with **arg

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

get_profile = build_profile('mumtaz', 'maqsood', location='Copenhagen', field = 'IT')
print(get_profile)

#TRY IT YOURSELF
#8-12 Sandwiches
#with for loop
def make_sandwich(*items):
    print(f"\n following Sandwich items included:")
    for item in items:
        print(item)

make_sandwich('tuna', 'mushrooms', 'tomato', 'onion')
make_sandwich('tuna', 'mushrooms', 'for loop')
print("----------------------------------------------")

#above example with while loop & return
def make_sandwich1(*items):
    print(f"\n following Sandwich items included:")
    while items:
        return f"{items}"

a = make_sandwich1('tuna', 'mushrooms', 'tomato', 'onion')
b = make_sandwich1('tuna', 'mushrooms')
print(a)
print(b)

#8-14 Cars
def car_info(manufacturer, model_name, **arg):
    arg['manufacturer'] = manufacturer
    arg['model_name'] = model_name
    return arg
car_dic = car_info('BMW', 'S', COLOR = 'BLUE', TOW_PACKAGE = 'True')
print(car_dic)






























