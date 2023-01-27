

from fun import get_formatted_name
print("Enter 'q' at any time to quit.")

while True:
    first_name = input("Enter your first name:")
    if first_name == 'q':
        break
    last_name = input("Enter your last name:")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first_name, last_name)
    print(f"\t Neatly formatte name: {formatted_name}")

