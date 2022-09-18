
names = ['gul andam', 'Shahbaz', 'Afnan', "test"]
print(names)

#list is the ordered collection of the data and can access list data by writing index
#print(names[0])
print(names[0].title())

# -1 return the last item in the list
print(names[-1])

#changing values in the list
names[3] = "Mumtaz"
print(names)

# append method use to add the list item in the end while insert method can add item anywhere in the list
#names.insert(index, 'data')
names.append("Fadia")
print(names)

# del statment use to remove the item in the list if position of the item is known
del names[3]
print(names)

#pop method use to remove the last item in the list but after that you can work on it
#pop method can also use by index and remove any item in the list pop(1) --> means remove 2nd item in the list
pop_list = names.pop()
print(f"after pop {names}: popped value: {pop_list}")


#remove remove the value when dont know about the position of the list items
names.remove('Afnan')
print(names)


#TRY IT YOURSELF
guest_list = ['Jens', 'Jesper', 'Tom']
print(f"{guest_list[0]}, you are invited for dinner")
print(f"{guest_list[1]}, you are invited for dinner")
print(f"{guest_list[2]}, you are invited for dinner")

pop_guest_list = guest_list.pop()
print(f"{pop_guest_list}, can't make the dinner")
guest_list.append("Morten")
print(f"modified guest list: {guest_list}")

print(f"Hi {guest_list[0]}, Found bigger table")
print(f"Hi {guest_list[1]}, Found bigger table")
print(f"Hi {guest_list[2]}, Found bigger table")

guest_list.insert(0, "Tavs")
guest_list.insert(3, "Marcus")
guest_list.append("Heidi")
print(f"updated guest list: {guest_list}")
print(f"{guest_list[0]}, you are invited for dinner")
print(f"{guest_list[1]}, you are invited for dinner")
print(f"{guest_list[2]}, you are invited for dinner")
print(f"{guest_list[3]}, you are invited for dinner")
print(f"{guest_list[4]}, you are invited for dinner")
print(f"{guest_list[5]}, you are invited for dinner")

print(" Can invite only two people for dinner.")
print(f"I am sorry cannot invite you for dinner :{guest_list.pop()}")
print(f"I am sorry cannot invite you for dinner :{guest_list.pop()}")
print(f"I am sorry cannot invite you for dinner :{guest_list.pop()}")
print(f"I am sorry cannot invite you for dinner :{guest_list.pop()}")

print(f"{guest_list[0]}, you are still invited for dinner")
print(f"{guest_list[1]}, you are still invited for dinner")

del guest_list[0]
del guest_list[0]
print(f"Empty list: {guest_list}")




#sort method use to sort the list permanently, can also accept sort(reverse= True)
cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort()
cars.sort(reverse= True)
print(cars)

#sorted function used to sort the list temporarily 
print(sorted(cars))
print(cars)
