
#looping with list

magicians = ['david', 'carolina', 'alice', 'test']

for magician in magicians:
    print(magician)

#4.1   TRY IT YOURSELF

pizzas = ['salat pizza', 'meat pizza', 'veg pizza']
for pizza in pizzas:
    print(f"I like {pizza}")
print("I really love pizza!")

#range() function help to create set of numbers
for no in range(1,5):
    print(no)


list_no = list(range(2,11,2))
#print(list_no)

#Try IT YOURSELF

#4-3 Counting to Twenty
numbers = list(range(1,21))
for no in numbers:
    print(no)

#4-4, 4-5 One Million
million_no = list(range(1,1000001))
# for no in million_no:
#     print(no)
print(min(million_no))
print(max(million_no))
print(sum(million_no))

#4-6 Odd Numbers
odd_no = list(range(1,21,2))
for no in odd_no:
    print(f"odd no list: {no}")

#4-7 Threes
threes = list(range(3,31, 3))
for no in threes:
    print(no)

#4-8 cubes

cubes = []
for no in range(1, 11):
    cube = no ** 3
    cubes.append(cube)
print(cubes)
for cube in cubes:
    print(cube)

#4-9 cube comprehension

cube_com = [no ** 3 for no in list(range(1, 11))]
print(cube_com)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())



#Copying list using a slice

my_foods = ['pizza', 'falafel', 'carrot cake']
frnd_food = my_foods[:]
my_foods.append("test")
frnd_food.append("meat")
print(my_foods)
print(frnd_food)



#TRY IT YOURSELF
# 4-10 Slice
print(my_foods[:3])
print(my_foods[1:3])


# Tuple --> is also a list but it cannot be changed called immutable while list can change and called mutable
dimensions = (100, 200)
for dimension in dimensions:
    print(dimension)

dimensions = (200,300)
for dimension in dimensions:
    print(dimension)


#TRY IT YOURSELF
#4-13 Buffet

buffet = ('food1','food2','food3','food4','food5')
for buffet_menu in buffet:
    print(buffet_menu)

buffet = ('food1','food2','food3','food4','food5', 'food6', 'food7')
for buffet_menu in buffet:
    print(f"updated menu \n - {buffet_menu}")









































