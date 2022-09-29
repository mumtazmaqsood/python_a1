
favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1000_000,
    'maggie': 0,
    }

for key, value in favorite_numbers.items():
    print(f"Key: {key}: Value: {value} ")
    #print(f"Value: {value}")


#-------------------------------------------------------------------
print("\n New Program")
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"{name.title()}, you like language: {language}!")

if 'mumtaz' not in favorite_languages.keys():
    print("Please take our poll!")

# sorted() function use to sort the dic keys
#set() function use to omit the key duplication

print("use of set() --> new program")
for lan in set(favorite_languages.values()):
    print(f"{lan}")

#TRY IT YOURSELF
#6-4- Glossary 2
print("6-4--------------")
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for key, value in glossary.items():
    print(f"{key.title()}: {value}")

#6-5 Rivers
print("\n---------------------------------------")
rivers = {
    'nile': 'egypt',
    'punjab': 'pakistan',
    'sindh': 'india'
}

for key, value in rivers.items():
    print(f"{key.title()} runs through {value.title()}")
print("\n---------------------------------------")

for key in rivers.keys():
    print(f"river name:{key}")
for value in rivers.values():
    print(f"country name:{value}")


print("\n------------6-6. Polling---------------------------")

favorite_languages1 = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }


for key, value in favorite_languages1.items():
    print(f"{key}:{value}")

print("\n")

persons = ['phil', 'josh', 'david', 'becca']
for person in persons:
    if person in favorite_languages1.keys():
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, what's your favorite programming language?")


print("\n------------end 6-6. Polling---------------------------")













