



name = "Mumtaz Maqsood"
print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

'----------------------------------------------------------'
'rstrip() --> remove whitespaces at the end of the string'
'lstrip() --> remove whitespaces at the begining of the string'
'strip() --> remove whitespaces in both sides '

var = "test  "
var1 = " test"
var2 = "    test2    "
var = var.rstrip()
var1 = var1.lstrip()
var2 = var2.strip()

print(var)
print(var1)
print(var2)
'---------------------------------------------------'

print(var[::-1])

print("------------string slicing------------")
name = 'python '
# print(name[-1])

print(f"name[0:0]:{name[:]}")

print(f"name[2:4]:{name[2:4]}")
print(f"name[0:3]:{name[0:3]}")
print(f"name[2:]:{name[2:]}")
print(f"name[-5:]:{name[-5:]}")
print(f"name[-6:]:{name[-6:]}")
print(f"name[-5:6]:{name[-5:5]}")

name1 = "mumtaz"[-1::-1]
print(f"Mumtaz[-1::-1] {name1}")
name2 = input("Enter your name:")
print(name2[::-1])

print("this is for test")
