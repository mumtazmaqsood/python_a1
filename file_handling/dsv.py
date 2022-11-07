# Import Module
import os

# Folder Path
path = "C:\\Users\\MumtazMaqsood\\Downloads\\sample_data\\output"

# Change the directory
os.chdir(path)

# Read text File
def read_text_file(file_path):
	with open(file_path, 'r') as f:
		print(f.read())


i = 0
file_titles = []

# iterate through all file
for file in os.listdir():

	# Check whether file is in text format or not
	if file.endswith(".tst"):
		i += 1
		file_titles.append(file.title())
		print(f"File Name:{file.title()}, length of file Name:{len(file.title())}")
		file_path = f"{path}\\{file}"


		# call read text file function
		read_text_file(file_path)
print(f"Total files: {i}")

valid_file_name_length = []
inValid_file_name_length = []
for file_title in file_titles:
	if file_title[11:15] == "_Dne" and len(file_title) == 19:
		valid_file_name_length.append(file_title)
	else:
		inValid_file_name_length.append(file_title)

print(f"Valid File Names and lenght:{valid_file_name_length}")
print(f"inValid File Names and lenght:{inValid_file_name_length}")