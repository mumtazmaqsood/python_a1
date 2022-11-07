import csv
#detials in python doc file in google drive
# with open("data.txt", "r+") as f:
#     f.seek(len(f.read()))
#     f.write("\n after seek method applying n")

# with open("Book1.csv", "r") as f:
#     csv_content = csv.reader(f)
#     get_csv_content = []
#     for content in csv_content:
#         get_csv_content += content
# for i in get_csv_content:
#     print(i)
# print(f"{get_csv_content}")

import json

# Opening JSON file
f = open('ab1.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for value in data:
    print(f"Value: {value['ID']} ")

# Closing file
f.close()