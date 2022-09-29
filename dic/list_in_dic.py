
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
}

print(f"you ordered a pizza {pizza['crust']} crust-pizza "
      f"with following toppings:")
for topping in pizza['toppings']:
    print(f"  {topping}")

print("favourite languages-------------------")
#favorite languages
favorite_languages = {
    'mumtaz': ['python', 'js', 'c'],
    'jens': ['rust', 'python'],
    'jesper': ['js']
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()} favourite languages:")
    else:
        print(f"{name.title()} favourite language:")
    for language in languages:
        print(f"{language.title()}")


#Dic within Dic
print("---------------------------------------------")
users = {
    'mumtaz': {
        'first_name': 'mumtaz',
        'last_name': 'maqsood',
        'location': 'Pakistan'
    },
    'fadia': {
        'first_name': 'fadia',
        'last_name': 'shafiq',
        'location': 'copenhagen'
    }
}

for user_name, user_info in users.items():
    print(f"{user_name}")
    print(f"Full Name: {user_info['first_name']} {user_info['last_name']}")
    print(f"location: {user_info['location']}")
    # for key, value in user_info.items():
    #     print(f"{key}: {value}")
print("---------------------------------------------")

#TRY IT YOURSELF
print("----------TRY IT YOURSELF -----------------------------------")
print("---------------#6-7 People------------------------------")
# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 46,
    'city': 'sitka',
    }
people.append(person)
person = {
    'first_name': 'mumtaz',
    'last_name': 'maqsood',
    'age': 44,
    'city': 'copenhagen',
    }
people.append(person)

person = {
    'first_name': 'saeed',
    'last_name': 'yousaf',
    'age': 40,
    'city': 'gujrat',
    }
people.append(person)
for person in people:
    print(f"{person['first_name'].title()}, {person['last_name'].title()}, {person['age']}, {person['city'].title()}")
print("---------------#6-7 People------------------------------")
print("----------END TRY IT YOURSELF -----------------------------------")





















