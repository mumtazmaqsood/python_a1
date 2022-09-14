
words = ['a', 'b', 'c', 'd', 'e']
print(words[:2])
print(words[-1])




# define a function take list input and return reversed list

def reverse_list(l):
    reverse_list = []
    for i in range(len(l)):
        reverse_list.append(l.pop())
    return  reverse_list
print(reverse_list(['a', 'b', 'c', 'd', 'e']))


#define a function that take list of words as argument and return list with reverse of every element in that list

def reverse_list1(l):
    empty_list = []
    for i in l:
        empty_list.append(i[::-1])
    return empty_list

a = reverse_list1(['abc', 'bde', 'chjkk', 'dddd', 'eeeee'])
print(a)



print("Assignment")


# i = 0
# while i < 10:
#     if i % 2 == 0:
#         i += 2
#         print(f"inside if i = {i}")
#         continue
#     else:
#         break
#     i += 1
#     print(f"outside if i={i}")
# print("completed")

#define a function that seperate even and odd and also write
#function with take input by user to create a custom list and every time ask
#user to quit the program if pressed q then program ends and display even and odd
#lists otherwise it continou until user not pressed q

def seperate_even_odd(l):
    even_list = []
    odd_list = []
    for i in range(len(l)):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list

# def create_list():
#     user_list = []
#     Flag = True
#     while Flag:
#         want_quit = input("Do you want to quit")
#         if want_quit == 'q':
#             Flag = False
#         else:
#             user_input = int(input("create your list:"))
#             user_list.append(user_input)
#     return user_list
#
# result = seperate_even_odd(create_list())
# print(result)



#create a function that take two lists of input and make a seperate common list

def make_common_list(l1,l2):
    common_list = []
    for i in l1:
        print(f"for i in l1:{i}")
        if i in l2:
            common_list.append(i)
    return common_list
result = make_common_list([1,2,3], [2,3,4,5,6])
print(result)














