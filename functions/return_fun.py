
# def get_formatted_name(first_name, last_name):
#     """Return a full name --> funciton"""
#     full_name = f"{first_name} {last_name}"
#     return full_name
#
# print(get_formatted_name('test', 'maqsood'))
# muscian = get_formatted_name('mumtaz', 'maqsood')
# print(muscian)


# optional parameter
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name --> funciton"""
    if middle_name:
        full_name = f"First Name: {first_name} Middle Name: {middle_name} Last Name:{last_name}"
    else:
        full_name = f"First Name:{first_name} Last Name:{last_name}"
    return full_name

print(get_formatted_name('Mr','Mumtaz', 'maqsood'))
muscian = get_formatted_name('mumtaz', 'maqsood')
print(muscian)



#Return a Dictionary
def return_dic(emplyee_name, department, post, age= None):
    employee_data = {'Employee Name': emplyee_name, 'Department': department, 'Job': post}
    if age:
        employee_data['age'] = age
    return employee_data

get_data = return_dic('Mumtaz maqsood', 'Qauality', 'QA Engineer', 40)
print(get_data)

#using while loop with above function -->get_formatted_name()

# while True:
#     print(f"\n Tell Your Name: ")
#     print("Enter q to quit the program")
#     f_name = input("Enter your First Name:")
#     if f_name == 'q':
#         break
#     l_name = input("Enter your Last Name:")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#
#     print(f"\nHello, {formatted_name}!")

#8-7 Album

def make_album(artist_name, album_title, no_of_songs= None):
    music_album = {'Artist Name': artist_name,
                   'Album Title': album_title,
                   }
    if no_of_songs:
        music_album['No.of Songs'] = no_of_songs
    return music_album

while True:
    print("\n q = quit program")
    artist_name = input("Enter artist name:")
    if artist_name == 'q':
        break
    album_title = input("Enter album title")
    if album_title == 'q':
        break
    ma = make_album(artist_name, album_title)
    print(ma)
# ma = make_album('Sara', 'Sara title', 10)
# print(f"{ma}")







