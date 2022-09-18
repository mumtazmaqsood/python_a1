
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y-position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'
print(alien_0)

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_1['speed'] = 'fast'
print(f"Original position: {alien_1['x_position']}")
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"New Position: {alien_1['x_position']}")


#defining new dic
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

print(f"{favorite_languages}")

#KeyError --> occurs when try to access the key that are not present in the dic
# use the get method --> first is the arg is "key" and msg(optional)
# get('key', 'msg')
other_name = favorite_languages.get('mumtaz', 'No key ')
print(other_name)


#TRY IT YOURSELF
#6-1 Person
person = {
    'first_name': 'Mumtaz',
    'last_name': 'Maqsood',
    'age': 42,
    'city': 'Copenhagen'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#6-2 Favorite Numbers
favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1000_000,
    'maggie': 0,
    }

#mandy = favorite_numbers['mandy']
num = favorite_numbers['mandy']
print(f"Mandy's favorite number is {num}.")

num = favorite_numbers['micah']
print(f"Micah's favorite number is {num}.")

num = favorite_numbers['gus']
print(f"Gus's favorite number is {num}.")

num = favorite_numbers['hank']
print(f"Hank's favorite number is {num}.")

num = favorite_numbers['maggie']
print(f"Maggie's favorite number is {num}.")



#6-3 Glossary
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
print("6-3--> Glossary")
word = 'string'
print(f"{word.title()}: {glossary[word]}")
word = 'comment'
print(f"{word.title()}: {glossary[word]}")
word = 'loop'
print(f"{word.title()}: {glossary[word]}")
word = 'dictionary'
print(f"{word.title()}: {glossary[word]}")






